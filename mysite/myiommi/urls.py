from django.urls import path
from iommi import Form, Table

from .models import Album, Artist
from .views import TopPage

urlpatterns = [
    path("", TopPage().as_view()),
    path("albums/", Table(auto__model=Album).as_view()),
    path("albums/create", Form.create(auto__model=Album, extra__redirect_to=".").as_view()),
    path("artists/", Table(auto__model=Artist).as_view()),
    path("artists/create", Form.create(auto__model=Artist, extra__redirect_to=".").as_view()),
]
