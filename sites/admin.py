from django.contrib import admin
from .models import Site, Rating, Tag
# Register your models here.

admin.site.register(Site)
admin.site.register(Rating)
admin.site.register(Tag)