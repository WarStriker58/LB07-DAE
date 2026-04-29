from django.db import models
from actors.models import Actor  # NUEVO


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()

    genres = models.ManyToManyField(Genre, related_name="movies")

    # NUEVO
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title