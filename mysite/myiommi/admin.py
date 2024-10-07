from django.contrib import admin

from .models import Album, Artist, Genre, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artist",
        "year",
    )


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TrackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "index",
        "album",
        "duration",
    )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
