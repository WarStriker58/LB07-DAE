from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()

# NUEVO
router.register('genres', GenreViewSet, basename='genres')

router.register('movies', MovieViewSet, basename='movies')

urlpatterns = router.urls