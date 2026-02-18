from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from .models import Task

# Create your views here.
def home_view(request):
    return render(request, "test.html")


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class TaskListView(ListView):
    model = Task
    template_name = "task/task_list_view.html"
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    template_name = "task/task_detail_view.html"