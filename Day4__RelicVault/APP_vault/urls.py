from django.urls import path

from .views import ItemListView, ItemDetailView, ItemUpdateView, ItemCreateView, ItemDeleteView, CharacterListView, CharacterDetailView, CharacterCreateView, CharacterUpdateView, home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("item/list/", ItemListView.as_view(), name="item_list_view"),
    path("item/details/<int:pk>/", ItemDetailView.as_view(), name="item_detail_view"),
    path("item/update/<int:pk>/", ItemUpdateView.as_view(), name="item_update_view"),
    path("item/create/", ItemCreateView.as_view(), name="item_create_view"),
    path("character/list/", CharacterListView.as_view(), name="character_list_view"),
    path("character/details/<int:pk>/", CharacterDetailView.as_view(), name="character_detail_view"),
    path("character/create/", CharacterCreateView.as_view(), name="character_create_view"),
    path("character/update/<int:pk>/", CharacterUpdateView.as_view(), name="character_update_view"),

]
