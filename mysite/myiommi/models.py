from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
)


class Artist(Model):
    name = CharField(max_length=255, db_index=True)


class Genre(Model):
    name = CharField(max_length=255, db_index=True)


class Album(Model):
    name = CharField(max_length=255, db_index=True)
    artist = ForeignKey(Artist, on_delete=CASCADE, related_name="albums")
    year = IntegerField(default=1980)
    genres = ManyToManyField(Genre, related_name="albums")


class Track(Model):
    name = CharField(max_length=255, db_index=True)
    index = IntegerField()
    album = ForeignKey(Album, on_delete=CASCADE, related_name="tracks")
    duration = CharField(max_length=255, db_index=False, null=True, blank=True)
