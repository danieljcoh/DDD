from django.urls import path

from .views import QuestBoardListView, QuestBoardDetailView, QuestBoardCreateView, QuestBoardDeleteView, QuestBoardUpdateView

urlpatterns = [
    path("", QuestBoardListView.as_view(), name="quest_list_view"),
    path("quest/<int:pk>/", QuestBoardDetailView.as_view(), name="quest_detail_view"),
    path("quest/<int:pk>/update/", QuestBoardUpdateView.as_view(), name="quest_update_view"),
    path("quest/<int:pk>/delete/", QuestBoardDeleteView.as_view(), name="quest_delete_view"),
    path("quest/new/", QuestBoardCreateView.as_view(), name="quest_new_view"),
]