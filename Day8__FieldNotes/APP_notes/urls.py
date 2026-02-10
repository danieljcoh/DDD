from django.urls import path

from .views import HomeTemplateView, LoginView, LogoutView, SignUpView, FieldNotesListView, FieldNotesCreateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),

    path("fieldnote/create/", FieldNotesCreateView.as_view(), name="fieldnotes_create_view"),
    path("fieldnotes/", FieldNotesListView.as_view(), name="fieldnotes_list_view"),

]