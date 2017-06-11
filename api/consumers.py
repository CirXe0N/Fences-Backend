import json
from datetime import datetime
from channels import Group
from channels.sessions import channel_session
from api.models import GameRoom


@channel_session
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    room_id = message.content['path'].strip("/")

    try:
        room = GameRoom.objects.get(room_id=room_id)

        message.channel_session['room_id'] = room_id
        Group("chat-%s" % room_id)
        group = Group("chat-%s" % room_id)
        group.add(message.reply_channel)

        content = {
            'type': 'CONNECT',
            'sent_at': datetime.now().isoformat()
        }

        if room.player_two:
            room.player_two_reply_channel = message.reply_channel
            content['user_id'] = '%s' % room.player_one
            group.send({"text": json.dumps(content)})

            content['user_id'] = '%s' % room.player_two
            group.send({"text": json.dumps(content)})
        else:
            room.player_one_reply_channel = message.reply_channel
        room.save()

    except GameRoom.DoesNotExist:
        pass


@channel_session
def ws_disconnect(message):
    room_id = message.channel_session['room_id']
    group = Group("chat-%s" % room_id)

    content = {
        'type': 'DISCONNECT',
        'sent_at': datetime.now().isoformat()
    }

    group.send({"text": json.dumps(content)})

    rooms = GameRoom.objects.filter(room_id=room_id)
    for room in rooms:
        room.delete()

    Group("chat-%s" % room_id).discard(message.reply_channel)


@channel_session
def ws_message(message):
    content = json.loads(message.content['text'])

    if content.get('type') == 'MESSAGE':
        content['sent_at'] = datetime.now().isoformat()

    room_id = message.channel_session['room_id']
    group = Group("chat-%s" % room_id)
    group.send({"text": json.dumps(content)})

