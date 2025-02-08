from django.db import models
from django.conf import settings
import uuid

class SustainableAction(models.Model):
    CATEGORIES = [
        ('RECYCLING', 'Reciclagem'),
        ('ENERGY', 'Energia'),
        ('WATER', 'Água'),
        ('MOBILITY', 'Mobilidade'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actions")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.category}"
