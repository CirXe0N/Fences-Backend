from rest_framework import serializers

from api.models import GameRoom


class GameRoomSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    player_one = serializers.UUIDField(write_only=True)
    player_two = serializers.UUIDField(write_only=True, allow_null=True)

    def get_user_id(self, obj):
        return self.initial_data['user_id']

    class Meta:
        model = GameRoom
        fields = ('room_id', 'user_id', 'player_one', 'player_two')
