from rest_framework import serializers
from .models import Movie, Genre
from actors.models import Actor  # NUEVO
from actors.serializers import ActorSerializer  # NUEVO


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)  # NUEVO

    class Meta:
        model = Movie
        fields = "__all__"