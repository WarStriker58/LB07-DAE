from rest_framework.routers import DefaultRouter
from .views import ActorViewSet

router = DefaultRouter()
router.register('actors', ActorViewSet, basename='actors')  # NUEVO

urlpatterns = router.urls