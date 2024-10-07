from django.contrib import admin

from .models import Album, Artist, Genre, Track

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Track)
