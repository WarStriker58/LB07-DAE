from django.contrib import admin
from .models import Movie, Genre

# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year')
    search_fields = ('title',)

    # NUEVO: permite seleccionar géneros en el admin
    filter_horizontal = ("genres",)  # IMPORTANTE