from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Item, Character


## HOME VIEW ##
def home_view(request):
    return render(request, "home.html")


## ITEM VIEWS ##
## ITEM VIEWS ##
class ItemListView(ListView):
    model = Item
    template_name = "item_list_view.html"

class ItemCreateView(CreateView):
    model = Item
    template_name = "item_create_view.html"
    fields = ["name", "value", "holder"]
    success_url = reverse_lazy("item_list_view")

class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail_view.html"

class ItemUpdateView(UpdateView):
    model = Item
    fields = ["name", "value", "holder"]
    template_name = "item_update_view.html"
    success_url = reverse_lazy("item_list_view")

class ItemDeleteView(DeleteView):
    pass


## CHARACTER VIEWS ##
## CHARACTER VIEWS ##
class CharacterListView(ListView):
    model = Character
    template_name = "character_list_view.html"

class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_create_view.html"
    fields = ["player_character_name", "player_name"]
    success_url = reverse_lazy("character_list_view")

class CharacterDetailView(DetailView):
    model = Character
    template_name = "character_detail_view.html"

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "character_update_view.html"
    fields = ["player_character_name", "player_name"]
    success_url = reverse_lazy("character_list_view")

