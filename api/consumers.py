import json
from datetime import datetime
from channels import Group
from channels.sessions import channel_session
from api.models import GameRoom


@channel_session
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    room_id = message.content['path'].strip("/")
    room = GameRoom.objects.get(room_id=room_id)
    # TODO Refactor this
    if room.player_two:
        room.player_two_reply_channel = message.reply_channel
    else:
        room.player_one_reply_channel = message.reply_channel
    room.save()
    message.channel_session['room_id'] = room_id
    Group("chat-%s" % room_id).add(message.reply_channel)


@channel_session
def ws_disconnect(message):
    room_id = message.channel_session['room_id']
    Group("chat-%s" % room_id).discard(message.reply_channel)


@channel_session
def ws_message(message):
    content = json.loads(message.content['text'])
    content['sent_at'] = datetime.now().isoformat()
    room_id = message.channel_session['room_id']
    Group("chat-%s" % room_id).send({"text": json.dumps(content)})

