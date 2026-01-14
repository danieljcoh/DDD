from django.urls import path

from .views import SpellbookListView, SpellbookCreateView, SpellbookDetailView

urlpatterns = [
    path("", SpellbookListView.as_view(), name="home"),
    path("spellbook/spell/add", SpellbookCreateView.as_view(), name="spell_create_view"),
    path("spellbook/spell/<int:pk>/", SpellbookDetailView.as_view(), name="spell_detail_view"),
    # path("spellbook/spell/search", name="spell_search_view")
    
]
