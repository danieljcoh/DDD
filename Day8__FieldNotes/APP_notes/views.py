from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FieldNote
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "home.html"


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"


class LogoutView(auth_views.LogoutView):
    pass


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        return redirect(self.success_url)
    

class FieldNotesListView(LoginRequiredMixin, ListView):
    model = FieldNote
    template_name = "fieldnotes/fieldnotes_list_view.html"

class FieldNotesCreateView(LoginRequiredMixin, CreateView):
    model = FieldNote
    template_name = "fieldnotes/fieldnote_create_view.html"
    fields = ["title", "information_text"] #add a picture later
    success_url = reverse_lazy("fieldnotes_list_view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    