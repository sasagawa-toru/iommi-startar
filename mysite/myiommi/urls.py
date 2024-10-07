from django.urls import path
from iommi import Form

from .models import Album, Artist

urlpatterns = [
    path("albums/create", Form.create(auto__model=Album).as_view()),
    path("artists/create", Form.create(auto__model=Artist).as_view()),
]
