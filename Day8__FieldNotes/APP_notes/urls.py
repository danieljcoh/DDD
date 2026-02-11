from django.urls import path

from .views import HomeListView, LoginView, LogoutView, SignUpView, FieldNotesListView, FieldNotesCreateView, FieldNotesDetailView, FieldNotesUpdateView, FieldNotesDeleteView
from .views import ToggleConfirmationView

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),

    path("fieldnote/create/", FieldNotesCreateView.as_view(), name="fieldnotes_create_view"),
    path("fieldnotes/", FieldNotesListView.as_view(), name="fieldnotes_list_view"),
    path("fieldnotes/details/<str:username>/<slug:slug>/", FieldNotesDetailView.as_view(), name="fieldnotes_detail_view"),
    path("fieldnotes/update/<str:username>/<slug:slug>/", FieldNotesUpdateView.as_view(), name="fieldnotes_update_view"),
    path("fieldnotes/delete/<str:username>/<slug:slug>/", FieldNotesDeleteView.as_view(), name="fieldnotes_delete_view"),

    path("fieldnotes/details/<str:username>/<slug:slug>/confirm/", ToggleConfirmationView.as_view(), name="fieldnotes_toggle_confirm"),

]