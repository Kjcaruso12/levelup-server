"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from levelupapi.models import Game
from levelupapi.models.GameType import GameType
from levelupapi.models.Gamer import Gamer
from django.db.models import Count
from django.db.models import Q

class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        try:
            gamer = Gamer.objects.get(user=request.auth.user)
            games = Game.objects.annotate(event_count=Count('events'),
                                          user_event_count=Count(
                                              'events',
                                              filter=Q(events=gamer)
                                          ))
            game_type = request.query_params.get('type', None)
            if game_type is not None:
                games = games.filter(gametype_id=game_type)

            serializer = GameSerializer(games, many=True)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        gamer = Gamer.objects.get(pk=request.data['gamer_id'])
        game_type = GameType.objects.get(pk=request.data['gametype'])
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, gametype=game_type)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=pk)
        serializer = CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    # gamer = GamerSerializer(many=False)
    # gametype = GameTypeSerializer(many=False)
    # event_count = serializers.IntegerField(default=None)
    # user_event_count = serializers.IntegerField(default=None)
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'gamer', 'number_of_players', 'skill_level', 'gametype')
        depth = 2

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'maker', 'number_of_players', 'skill_level', 'gamer', 'gametype']
        depth = 2