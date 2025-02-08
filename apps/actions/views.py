from rest_framework import viewsets, permissions
from .models import SustainableAction
from .serializers import SustainableActionSerializer
from django.views.generic import TemplateView

class SustainableActionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SustainableActionSerializer

    def get_queryset(self):
        return SustainableAction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        action = serializer.save(user=self.request.user)
        user = self.request.user
        if hasattr(user, 'points'):
            user.points += action.points
            user.save()

    def perform_update(self, serializer):
        action = serializer.save()
        user = self.request.user
        if hasattr(user, 'points'):
            user.points = sum(SustainableAction.objects.filter(user=user).values_list('points', flat=True))
            user.save()
