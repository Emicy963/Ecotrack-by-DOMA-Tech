from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SustainableActionViewSet

router = DefaultRouter()
router.register(r'actions', SustainableActionViewSet, basename='action')

urlpatterns = router.urls