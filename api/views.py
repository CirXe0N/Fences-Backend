from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import GameRoom
from api.serializers import GameRoomSerializer
import uuid


@api_view(['GET', 'POST'])
def get_or_create_game_room(request):
    print('test')
    if request.method == 'GET':
        room = GameRoom.objects.filter(player_two__isnull=True, player_one_reply_channel__isnull = False).first()
        user_id = uuid.uuid4()

        if room:
            serializer = GameRoomSerializer(room, data={'user_id': user_id, 'player_two': user_id}, partial=True)
        else:
            serializer = GameRoomSerializer(data={'user_id': user_id, 'player_one': user_id}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

