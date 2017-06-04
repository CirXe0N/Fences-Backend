import uuid
from django.db import models


class GameRoom(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_one = models.UUIDField()
    player_one_reply_channel = models.CharField(max_length=50, null=True)
    player_two = models.UUIDField(null=True)
    player_two_reply_channel = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
