from django.contrib import admin

from .models import Album, Artist, Genre, Track


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track)
