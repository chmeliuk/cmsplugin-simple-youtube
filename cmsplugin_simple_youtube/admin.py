from django.contrib import admin
from models import SimpleYouTube

class SimpleYouTubeAdmin(admin.ModelAdmin):
    list_display = ('thumbnail','name', 'video_url', 'autoplay',)
    pass

admin.site.register(SimpleYouTube, SimpleYouTubeAdmin)
