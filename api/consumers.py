import json
from datetime import datetime
from channels import Group


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def ws_message(message):
    content = json.loads(message.content['text'])
    content['sent_at'] = datetime.now().isoformat()
    Group("chat").send({"text": json.dumps(content)})

