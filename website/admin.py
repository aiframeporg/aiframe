from django.contrib import admin
from .models import Blog, ModelPost, Tutorial
from .models import DownloadableApp

admin.site.register(DownloadableApp)
admin.site.register(Blog)
admin.site.register(ModelPost)
admin.site.register(Tutorial)
