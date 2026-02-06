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
    fields = ["first_name", "last_name", "player_character_name"]
    success_url = reverse_lazy("character_list_view")


class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "character/character_delete_view.html"
    success_url = reverse_lazy("character_list_view")



class ItemCreateView(CreateView):
    model = Item
    template_name = "item/item_create_view.html"
    fields = ["item_name", "item_description", "owner"]
    success_url = reverse_lazy("item_list_view")


class ItemListView(ListView):
    model = Item
    template_name = "item/item_list_view.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item/item_detail_view.html"


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "item/item_update_view.html"
    fields = ["item_name", "item_description", "owner"]
    success_url = reverse_lazy("item_list_view")

    def form_valid(self, form):
        item = self.get_object()
        old_owner = item.owner
        new_owner = form.cleaned_data["owner"]

        response = super().form_valid(form)

        if old_owner != new_owner:
            TransferLog.objects.create(
                item_transferred=self.object,
                transfer_from=old_owner,
                transfer_to=new_owner
            )
        return response


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "item/item_delete_view.html"
    success_url = reverse_lazy("item_list_view")


class TransferlogListView(ListView):
    model = TransferLog
    template_name = "transfer_log/transferlog_list_view.html"