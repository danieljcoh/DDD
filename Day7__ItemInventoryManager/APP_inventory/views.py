from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

# Create your views here.

def homepage_view(request):
    return render(request, "home.html")


class CharacterCreateView(CreateView):
    model = Character
    template_name = "character/character_create_view.html"
    fields = ["first_name", "last_name", "player_character_name"]
    success_url = reverse_lazy("character_list_view")


class CharacterListView(ListView):
    model = Character
    template_name = "character/character_list_view.html"


class CharacterDetailView(DetailView):
    model = Character
    template_name = "character/character_detail_view.html"


class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "character/character_update_view.html"
    success_url = reverse_lazy("character_list_view")


class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "character/character_delete_view.html"
    success_url = reverse_lazy("character_list_view")
