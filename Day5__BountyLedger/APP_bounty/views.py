from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from .models import Outlaw, Bounty

## BOUNTY VIEWS ↓↓↓ ##
## BOUNTY VIEWS ↓↓↓ ##
class BountyListView(ListView):
    model = Bounty
    template_name = "bounty_list_view.html"


class BountyCreateView(CreateView):
    model = Bounty
    fields = ["title", "description", "rewarded_to"]
    template_name = "bounty_create_view.html"

    def get_success_url(self):
        return reverse_lazy("bounty_list_view")


class BountyUpdateView(UpdateView):
    model = Bounty
    fields = ["title", "description", "reward_amount", "rewarded_to"]
    template_name = "bounty_update_view.html"

    def form_valid(self, form):
        
        bounty_before = self.get_object()

        old_outlaw = bounty_before.rewarded_to
        old_reward = bounty_before.reward_amount

        new_outlaw = form.cleaned_data["rewarded_to"]
        new_reward = form.cleaned_data["reward_amount"]

        # Only adjust gold if payout-related fields changed
        if {"rewarded_to", "reward_amount"} & set(form.changed_data):

            # Undo old payout
            if old_outlaw:
                old_outlaw.total_gold -= old_reward
                old_outlaw.save()

            # Apply new payout
            if new_outlaw:
                new_outlaw.total_gold += new_reward
                new_outlaw.save()

        return super().form_valid(form)
        

    def get_success_url(self):
        return reverse_lazy("bounty_list_view")
    

class BountyDeleteView(DeleteView):
    model = Bounty
    template_name = "bounty_delete_view.html"

    def get_success_url(self):
        return reverse_lazy("bounty_list_view")
    

class BountyLeaderBoardView(ListView):
    model = Outlaw
    template_name = "leaderboard.html"
    context_object_name = "outlaws"
    queryset = Outlaw.objects.order_by("-total_gold")
    

## OUTLAW VIEWS ↓↓↓ ##
## OUTLAW VIEWS ↓↓↓ ##

class OutlawCreateView(CreateView):
    model = Outlaw
    fields = ["player_name", "player_character_name"]
    template_name = "outlaw_create_view.html"

    def get_success_url(self):
        return reverse_lazy("outlaw_list_view")
    
class OutlawListView(ListView):
    model = Outlaw
    template_name = "outlaw_list_view.html"

class OutlawDetailView(DetailView):
    model = Outlaw
    template_name = "outlaw_detail_view.html"

class OutlawUpdateView(UpdateView):
    model = Outlaw
    fields = ["player_name", "player_character_name"]
    template_name = "outlaw_update_view.html"

    def get_success_url(self):
        return reverse_lazy("outlaw_list_view")
    
class OutlawDeleteView(DeleteView):
    model = Outlaw
    template_name = "outlaw_delete_view.html"

    def get_success_url(self):
        return reverse_lazy("outlaw_list_view")