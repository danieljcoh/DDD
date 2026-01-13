from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Quest

# Create your views here.
class QuestBoardListView(ListView):
    model = Quest
    template_name = "quests_list.html"
    context_object_name = "quests"

class QuestBoardDetailView(DetailView):
    model = Quest
    template_name = "quest_details.html"

class QuestBoardCreateView(CreateView):
    model = Quest
    template_name = "quest_new.html"
    fields = ["title", "body", "difficulty", "reward", "open_or_closed"]
    success_url = reverse_lazy("quest_list_view") # I'm not sure that I need this...

class QuestBoardUpdateView(UpdateView):
    model = Quest
    template_name = "quest_edit.html"
    fields = ["title", "body", "difficulty", "reward", "open_or_closed"]
    success_url = reverse_lazy("quest_list_view")

class QuestBoardDeleteView(DeleteView):
    model = Quest
    template_name = "quest_delete.html"
    success_url = reverse_lazy("quest_list_view")