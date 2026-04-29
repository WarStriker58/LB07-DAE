# NUEVO - Script simple para data de prueba
import django
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinespoilers.settings')
django.setup()

from movies.models import Movie, Genre
from actors.models import Actor

def run():
    # Crear géneros
    genre_names = ["Action", "Drama", "Sci-Fi", "Comedy"]
    genres = [Genre.objects.get_or_create(name=g)[0] for g in genre_names]

    # Crear actores
    actor_names = ["Leonardo DiCaprio", "Scarlett Johansson", "Brad Pitt", "Emma Stone"]
    actors = [
        Actor.objects.get_or_create(name=a, birth_year=random.randint(1970, 2000))[0]
        for a in actor_names
    ]

    # Crear películas
    for i in range(5):
        movie = Movie.objects.get_or_create(
            title=f"Movie {i+1}",
            description="Sample description",
            release_year=2000 + i,
        )[0]

        movie.genres.set(random.sample(genres, 2))
        movie.actors.set(random.sample(actors, 2))

    print("✔ Datos de prueba generados correctamente")

if __name__ == "__main__":
    run()