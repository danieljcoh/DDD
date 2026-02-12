from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FieldNote, Confirmation
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class HomeListView(ListView):
    model = FieldNote
    template_name = "home.html"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return FieldNote.objects.none()
        return FieldNote.objects.filter(author=self.request.user).order_by("-created_at")


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
    

class FieldNotesListView(ListView):
    model = FieldNote
    template_name = "fieldnotes/fieldnotes_list_view.html"

    def get_queryset(self):
        return FieldNote.objects.filter(is_public=True).order_by("-created_at")

class FieldNotesCreateView(LoginRequiredMixin, CreateView):
    model = FieldNote
    template_name = "fieldnotes/fieldnote_create_view.html"
    fields = ["title", "information_text", "is_public"] #add a picture later
    success_url = reverse_lazy("fieldnotes_list_view")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class FieldNotesDetailView(DetailView):
    model = FieldNote
    template_name = "fieldnotes/fieldnotes_detail_view.html"

    def get_object(self):
        return get_object_or_404(
            FieldNote,
            author__username=self.kwargs["username"],
            slug=self.kwargs["slug"]
        )
    

class FieldNotesUpdateView(UpdateView):
    model = FieldNote
    template_name = "fieldnotes/fieldnotes_update_view.html"
    fields = ["title", "information_text", "is_public"]
    context_object_name = "fieldnote"

    def get_object(self):
        return get_object_or_404(
            FieldNote,
            author__username=self.kwargs["username"],
            slug=self.kwargs["slug"]
        )


class FieldNotesDeleteView(DeleteView):
    model = FieldNote
    template_name = "fieldnotes/fieldnotes_delete_view.html"
    success_url = reverse_lazy("fieldnotes_list_view")
    context_object_name = "fieldnote"

    def get_object(self):
        return get_object_or_404(
            FieldNote,
            author__username=self.kwargs["username"],
            slug=self.kwargs["slug"]
        )
    

class ToggleConfirmationView(LoginRequiredMixin, View):
    def post(self, request, username, slug):
        note = get_object_or_404(FieldNote, author__username=username, slug=slug)

        if not note.is_public:
            return redirect(note.get_absolute_url())
        
        confirmation, created = Confirmation.objects.get_or_create(
            scout=request.user,
            field_note=note
        )

        if not created:
            confirmation.delete()

        return redirect(note.get_absolute_url())