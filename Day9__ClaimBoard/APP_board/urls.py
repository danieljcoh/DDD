from django.urls import path

from .views import HomeTemplateView, TaskListView, DraftTaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views import LoginView, SignUpView,LogoutView
from .views import ToggleClaimView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/details/<str:username>/<slug:slug>/", TaskDetailView.as_view(), name="task_detail_view"),
    path("task/create/", TaskCreateView.as_view(), name="task_create_view"),
    path("task/drafts/", DraftTaskListView.as_view(), name="task_list_view_drafts"),
    path("task/update/<str:username>/<slug:slug>/", TaskUpdateView.as_view(), name="task_update_view"),
    path("task/delete/<str:username>/<slug:slug>/", TaskDeleteView.as_view(), name="task_delete_view"),

    path("task/details/<str:username>/<slug:slug>/confirm/", ToggleClaimView.as_view(), name="fieldnotes_toggle_confirm"),

    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
