from django.urls import path

from .views import BeastListView, BeastCreateView, BeastDetailView, BeastUpdateView, BeastDeleteView

urlpatterns = [
    path("", BeastListView.as_view(), name="beast_list_view"),
    path("create/", BeastCreateView.as_view(), name="beast_create_view"),
    path("beast/details/<int:pk>/", BeastDetailView.as_view(), name="beast_detail_view"),
    path("beast/update/<int:pk>/", BeastUpdateView.as_view(), name="beast_update_view"),
    path("beast/delete/<int:pk>/", BeastDeleteView.as_view(), name="beast_delete_view"),


]
