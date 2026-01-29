from django.urls import path

from .views import *

urlpatterns = [
    path("", home_page_view, name="home"),

    path("character/create/", CharacterCreateView.as_view(), name="character_create_view"),
    path("character/list/", CharacterListView.as_view(), name="character_list_view"),
    path("character/detail/<int:pk>/", CharacterDetailView.as_view(), name="character_detail_view"),
    path("character/update/<int:pk>/", CharacterUpdateView.as_view(), name="character_update_view"),
    path("character/delete/<int:pk>/", CharacterDeleteView.as_view(), name="character_delete_view"),

    path("creature/create/", CreatureCreateView.as_view(), name="creature_create_view"),
    path("creature/list/", CreatureListView.as_view(), name="creature_list_view"),
    path("creature/detail/<int:pk>/", CreatureDetailView.as_view(), name="creature_detail_view"),
    path("creature/update/<int:pk>/", CreatureUpdateView.as_view(), name="creature_update_view"),
    path("creature/delete/<int:pk>/", CreatureDeleteView.as_view(), name="creature_delete_view"),

    path("party/create/", PartyCreateView.as_view(), name="party_create_view"),
    path("party/list/", PartyListView.as_view(), name="party_list_view"),
    path("party/detail/<int:pk>/", PartyDetailView.as_view(), name="party_detail_view"),
    path("party/update/<int:pk>/", PartyUpdateView.as_view(), name="party_update_view"),
    path("party/delete/<int:pk>/", PartyDeleteView.as_view(), name="party_delete_view"),

    path("encounter/create/", EncounterCreateView.as_view(), name="encounter_create_view"),
    path("encounter/list/", EncounterListView.as_view(), name="encounter_list_view"),
    path("encounter/detail/<int:pk>/", EncounterDetailView.as_view(), name="encounter_detail_view"),
    path("encounter/update/<int:pk>/", EncounterUpdateView.as_view(), name="encounter_update_view"),
    path("encounter/delete/<int:pk>/", EncounterDeleteView.as_view(), name="encounter_delete_view"),

    path("encounterEntry/create/", EncounterEntryCreateView.as_view(), name="encounterEntry_create_view"),
    path("encounterEntry/list/", EncounterEntryListView.as_view(), name="encounterEntry_list_view"),
    path("encounterEntry/detail/<int:pk>/", EncounterEntryDetailView.as_view(), name="encounterEntry_detail_view"),
    path("encounterEntry/update/<int:pk>/", EncounterEntryUpdateView.as_view(), name="encounterEntry_update_view"),
    path("encounterEntry/delete/<int:pk>/", EncounterEntryDeleteView.as_view(), name="encounterEntry_delete_view"),
]
