from django.urls import path

from .views import CharacterCreateView, CharacterListView, CharacterDetailView, CharacterUpdateView, CharacterDeleteView
from .views import homepage_view

urlpatterns = [
    path("", homepage_view, name="home"),
    path("character/create/", CharacterCreateView.as_view(), name="character_create_view"),
    path("character/list/", CharacterListView.as_view(), name="character_list_view"),
    path("character/details/<int:pk>/", CharacterDetailView.as_view(), name="character_detail_view"),
    path("character/update/<int:pk>/", CharacterUpdateView.as_view(), name="character_update_view"),
    path("character/delete/<int:pk>/", CharacterDeleteView.as_view(), name="character_delete_view"),




]
