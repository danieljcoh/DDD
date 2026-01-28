from django.urls import path

from .views import BountyListView, BountyCreateView, BountyDeleteView, BountyLeaderBoardView, BountyUpdateView
from .views import OutlawCreateView, OutlawDeleteView, OutlawDetailView, OutlawListView, OutlawUpdateView

urlpatterns = [
    path("", BountyListView.as_view(), name="bounty_list_view"),
    path("bounty/create/", BountyCreateView.as_view(), name="bounty_create_view"),
    path("bounty/update/<int:pk>/", BountyUpdateView.as_view(), name="bounty_update_view"),
    path("bounty/delete/<int:pk>/", BountyDeleteView.as_view(), name="bounty_delete_view"),
    path("outlaw/", OutlawListView.as_view(), name="outlaw_list_view"),
    path("outlaw/create/", OutlawCreateView.as_view(), name="outlaw_create_view"),
    path("outlaw/detail/<int:pk>/", OutlawDetailView.as_view(), name="outlaw_detail_view"),
    path("outlaw/update/<int:pk>/", OutlawUpdateView.as_view(), name="outlaw_update_view"),
    path("outlaw/delete/<int:pk>/", OutlawDeleteView.as_view(), name="outlaw_delete_view"),
    path("outlaw/leaderboard/", BountyLeaderBoardView.as_view(), name="leaderboard_view")

]