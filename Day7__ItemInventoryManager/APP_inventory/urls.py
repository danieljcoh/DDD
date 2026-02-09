from django.urls import path

from .views import CharacterCreateView, CharacterListView, CharacterDetailView, CharacterUpdateView, CharacterDeleteView
from .views import homepage_view
from .views import ItemCreateView, ItemListView, ItemDetailView, ItemUpdateView, ItemDeleteView
from .views import TransferlogListView
from .views import LoginView, LogoutView


urlpatterns = [
    path("", homepage_view, name="home"),
    path("character/create/", CharacterCreateView.as_view(), name="character_create_view"),
    path("character/list/", CharacterListView.as_view(), name="character_list_view"),
    path("character/details/<int:pk>/", CharacterDetailView.as_view(), name="character_detail_view"),
    path("character/update/<int:pk>/", CharacterUpdateView.as_view(), name="character_update_view"),
    path("character/delete/<int:pk>/", CharacterDeleteView.as_view(), name="character_delete_view"),

    path("item/create/", ItemCreateView.as_view(), name="item_create_view"),
    path("item/list/", ItemListView.as_view(), name="item_list_view"),
    path("item/details/<int:pk>/", ItemDetailView.as_view(), name="item_detail_view"),
    path("item/update/<int:pk>/", ItemUpdateView.as_view(), name="item_update_view"),
    path("item/delete/<int:pk>/", ItemDeleteView.as_view(), name="item_delete_view"),

    path("transfer/", TransferlogListView.as_view(), name="transferlog_list_view"), 

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
