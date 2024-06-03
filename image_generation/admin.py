from django.contrib import admin
from .models import ImageGeneration

@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display=('title','user','created_at','updated_at')
    search_fields=('title','user__username')
    


