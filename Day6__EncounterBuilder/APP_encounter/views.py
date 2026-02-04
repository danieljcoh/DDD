from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from .models import Party, EncounterEntry, Encounter, Creature, Character


## FBVs ꜜꜜꜜ ##
## FBVs ꜜꜜꜜ ##
def home_page_view(request):
    return render(request, "home.html")


## CHARACTER VIEWS ꜜꜜꜜ ##
## CHARACTER VIEWS ꜜꜜꜜ ##
class CharacterCreateView(CreateView):
    model = Character
    template_name = "character_create_view.html"
    fields = ["player_name", "player_character_name", "party"]
    
    def get_success_url(self):
        return reverse_lazy("character_list_view")
    
class CharacterListView(ListView):
    model = Character
    template_name = "character_list_view.html"

class CharacterDetailView(DetailView):
    model = Character
    template_name = "character_detail_view.html"

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "character_update_view.html"
    fields = ["player_name", "player_character_name", "party"]

    def get_success_url(self):
        return reverse_lazy("character_detail_view", kwargs={"pk": self.object.pk})

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "character_delete_view.html"

    def get_success_url(self):
        return reverse_lazy("character_list_view")
    

## PARTY VIEWS ꜜꜜꜜ ##
## PARTY VIEWS ꜜꜜꜜ ##
class PartyCreateView(CreateView):
    model = Party
    template_name = "party_create_view.html"
    fields = ["name", "level", "size"]
    
    def get_success_url(self):
        return reverse_lazy("party_list_view")
    
class PartyListView(ListView):
    model = Party
    template_name = "party_list_view.html"

class PartyDetailView(DetailView):
    model = Party
    template_name = "party_detail_view.html"

class PartyUpdateView(UpdateView):
    model = Party
    template_name = "party_update_view.html"
    fields = ["name", "level", "size"]

    def get_success_url(self):
        return reverse_lazy("party_detail_view", kwargs={"pk": self.object.pk})

class PartyDeleteView(DeleteView):
    model = Party
    template_name = "party_delete_view.html"

    def get_success_url(self):
        return reverse_lazy("party_list_view")
    

## CREATURE VIEWS ꜜꜜꜜ ##
## CREATURE VIEWS ꜜꜜꜜ ##
class CreatureCreateView(CreateView):
    model = Creature
    template_name = "creature_create_view.html"
    fields = ["name", "threat_points"]
    
    def get_success_url(self):
        return reverse_lazy("creature_list_view")
    
class CreatureListView(ListView):
    model = Creature
    template_name = "creature_list_view.html"

class CreatureDetailView(DetailView):
    model = Creature
    template_name = "creature_detail_view.html"

class CreatureUpdateView(UpdateView):
    model = Creature
    template_name = "creature_update_view.html"
    fields = ["name", "threat_points"]
    
    def get_success_url(self):
        return reverse_lazy("creature_detail_view", kwargs={"pk": self.object.pk})
    
class CreatureDeleteView(DeleteView):
    model = Creature
    template_name = "creature_delete_view.html"
    
    def get_success_url(self):
        return reverse_lazy("creature_list_view")
    

## ENCOUNTER VIEWS ꜜꜜꜜ ##
## ENCOUNTER VIEWS ꜜꜜꜜ ##
class EncounterCreateView(CreateView):
    model = Encounter
    template_name = "encounter_create_view.html"
    fields = ["encounter_name", "party"]
    
    def get_success_url(self):
        return reverse_lazy("encounter_list_view")
    
class EncounterListView(ListView):
    model = Encounter
    template_name = "encounter_list_view.html"

class EncounterDetailView(DetailView):
    model = Encounter
    template_name = "encounter_detail_view.html"

class EncounterUpdateView(UpdateView):
    model = Encounter
    template_name = "encounter_update_view.html"
    fields = ["encounter_name", "party"]
    
    def get_success_url(self):
        return reverse_lazy("encounter_detail_view", kwargs={"pk": self.object.pk})
    
class EncounterDeleteView(DeleteView):
    model = Encounter
    template_name = "encounter_delete_view.html"
    
    def get_success_url(self):
        return reverse_lazy("encounter_list_view")
    

## ENCOUNTER_ENTRY VIEWS ꜜꜜꜜ ##
## ENCOUNTER_ENTRY VIEWS ꜜꜜꜜ ##
class EncounterEntryCreateView(CreateView):
    model = EncounterEntry
    template_name = "encounterEntry_create_view.html"
    fields = ["encounter", "creature", "quantity"]
    
    def get_success_url(self):
        return reverse_lazy("encounterEntry_list_view")
    
class EncounterEntryListView(ListView):
    model = EncounterEntry
    template_name = "encounterEntry_list_view.html"

class EncounterEntryDetailView(DetailView):
    model = EncounterEntry
    template_name = "encounterEntry_detail_view.html"

class EncounterEntryUpdateView(UpdateView):
    model = EncounterEntry
    template_name = "encounterEntry_update_view.html"
    fields = ["encounter", "creature", "quantity"]
    
    def get_success_url(self):
        return reverse_lazy("encounterEntry_detail_view", kwargs={"pk": self.object.pk})
    
class EncounterEntryDeleteView(DeleteView):
    model = EncounterEntry
    template_name = "encounterEntry_delete_view.html"
    
    def get_success_url(self):
        return reverse_lazy("encounterEntry_list_view")