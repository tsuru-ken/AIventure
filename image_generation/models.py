from django.db import models

from users.models import CustomUser

class ImageGenerration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='image_generation')
    title = models.CharField(max_length=255)
    description = models.TextField()
    generration_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    