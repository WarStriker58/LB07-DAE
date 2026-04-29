from rest_framework import serializers
from .models import Movie, Genre

# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    # CAMBIO
    genres = GenreSerializer(many=True)  # NUEVO

    class Meta:
        model = Movie
        fields = "__all__"