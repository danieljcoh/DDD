from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth import views as auth_views

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Claim
from django.contrib.auth.forms import UserCreationForm


##### Login/Logout/Signup #####
##### Login/Logout/Signup #####
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        return redirect(self.success_url)
    

class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"


class LogoutView(auth_views.LogoutView):
    pass


class HomeTemplateView(TemplateView):
    template_name = "home.html"



##### TASK CRUD #####
##### TASK CRUD #####
class TaskListView(ListView):
    model = Task
    template_name = "task/task_list_view.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.exclude(status__iexact="Draft").order_by("-date_created")
    

class DraftTaskListView(ListView):
    model = Task
    template_name = "task/task_list_view_drafts.html"
    context_object_name = "drafted_tasks"

    def get_queryset(self):
        return Task.objects.filter(status__iexact="Draft").order_by("-date_created")

class TaskDetailView(DetailView):
    model = Task
    template_name = "task/task_detail_view.html"

    # def get_object(self):
    #     return get_object_or_404(Task, author__username=self.kwargs["username"], slug=self.kwargs["slug"])

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task/task_create_view.html"
    fields = ["title", "task_information", "task_type", "status", "reward"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "task/task_update_view.html"
    fields = ["title", "task_information", "task_type", "status", "reward"]
    context_object_name = "task"

    def get_object(self):
        return get_object_or_404(
            Task,
            author__username=self.kwargs["username"],
            slug=self.kwargs["slug"]
        )


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "task/task_delete_view.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return get_object_or_404(
            Task,
            author__username=self.kwargs["username"],
            slug=self.kwargs["slug"]
        )


class ToggleClaimView(LoginRequiredMixin, View):
    def post(self, request, username, slug):
        task = get_object_or_404(Task, author__username=username, slug=slug)

        if not task.status == "Posted" and task.status != "claimed":
            return redirect(task.get_absolute_url())
        
        claim, created = Claim.objects.get_or_create(
            claimer=request.user,
            task=task
        )

        if not created:
            claim.delete()
        
        return redirect(task.get_absolute_url())
