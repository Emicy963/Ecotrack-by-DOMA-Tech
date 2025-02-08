from rest_framework import serializers
from .models import SustainableAction

class SustainableActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainableAction
        fields = ['id', 'title', 'description', 'category', 'points', 'created_at']
        read_only_fields = ['id', 'created_at']
