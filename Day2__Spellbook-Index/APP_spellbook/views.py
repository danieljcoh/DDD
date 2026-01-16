from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Spell

# Create your views here.

class SpellbookListView(ListView):
    model = Spell
    template_name = "spellbook_list_view.html"

    def get_queryset(self):
        query = super().get_queryset()
        searched_item = self.request.GET.get("search")
        if searched_item:
            filtered_query = query.filter(spell_name__icontains=searched_item)
            return filtered_query
        return query
    
class SpellbookCreateView(CreateView):
    model = Spell
    template_name = "spell_new.html"
    fields = ['spell_name', 'spell_mana_cost', 'spell_element_type', 
              'spell_ingredients', 'spell_directions', "spell_is_forbidden"]
    
class SpellbookDetailView(DetailView):
    model = Spell
    template_name = "spell_detail_view.html"


class SpellbookUpdateView(UpdateView):
    model = Spell
    template_name = "spell_update_view.html"
    fields = ['spell_name', 'spell_mana_cost', 'spell_element_type', 
              'spell_ingredients', 'spell_directions', "spell_is_forbidden"]
    success_url = reverse_lazy("spell_detail_view") # make sure this goes to the proper PK