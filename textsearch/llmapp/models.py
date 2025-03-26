from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TextGeneration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    summary = models.TextField(blank=True, null=True)
    bullet_points = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
