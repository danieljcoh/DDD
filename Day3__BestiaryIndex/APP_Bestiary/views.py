from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Beast

# Create your views here.

class BeastListView(ListView):
    model = Beast
    template_name = "beast_list.html"

    def get_queryset(self):
        query = super().get_queryset()
        order = self.request.GET.get("order")
        if order:
            if order == "asc":
                ordered_query = query.order_by("threat_level")
            elif order == "desc":
                ordered_query = query.order_by("-threat_level")
            return ordered_query
        return query

class BeastCreateView(CreateView):
    model = Beast
    template_name = "beast_create.html"
    fields = ["name", "found", "attack_power", "attack_speed", "defense", "threat_level", "is_legendary", "notable_attack", "quirky_behavior"]
    success_url = reverse_lazy("beast_list_view")

class BeastDetailView(DetailView):
    model = Beast
    template_name = "beast_detail.html"

class BeastUpdateView(UpdateView):
    model = Beast
    fields = ["name", "found", "attack_power", "attack_speed", "defense", "threat_level", "is_legendary", "notable_attack", "quirky_behavior"]
    template_name = "beast_update.html"
    
    def get_success_url(self):
        return reverse_lazy("beast_detail_view", kwargs={'pk': self.object.pk})

class BeastDeleteView(DeleteView):
    model = Beast
    template_name = "beast_delete.html"
    success_url = reverse_lazy("beast_list_view")

                      