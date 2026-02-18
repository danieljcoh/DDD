from django.urls import path

from .views import HomeTemplateView, TaskListView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/details/<int:pk>/", TaskDetailView.as_view(), name="task_detail_view"),
]
