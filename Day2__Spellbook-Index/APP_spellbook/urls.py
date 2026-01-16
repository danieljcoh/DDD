from django.urls import path

from .views import SpellbookListView, SpellbookCreateView, SpellbookDetailView, SpellbookUpdateView

urlpatterns = [
    path("", SpellbookListView.as_view(), name="home"),
    path("spellbook/spell/add", SpellbookCreateView.as_view(), name="spell_create_view"),
    path("spellbook/spell/<int:pk>/", SpellbookDetailView.as_view(), name="spell_detail_view"),
    path("spellbook/spell/<int:pk>/edit", SpellbookUpdateView.as_view(), name="spell_update_view"),
    
    
]
