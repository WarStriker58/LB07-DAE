from django.db import models

# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()

    # CAMBIO: antes era ForeignKey, ahora ManyToMany
    genres = models.ManyToManyField(Genre, related_name="movies")  # NUEVO

    def __str__(self):
        return self.title