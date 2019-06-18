from django.shortcuts import render
from IPLclone.models import *
from django.shortcuts import *
from django.views import *
# Create your views here.

class seasonClassView(View):
    def get(self, request, *args, **kwargs):
        match = seasons.objects.filter(**kwargs).values('match_id','team1', 'team2', 'venue', 'toss_winner','toss_decision', 'player_of_match')
        return render(
            request,
            template_name = 'seasons.html',
            context = {
                'match': match,
                'title': 'Match deatils'
            }
        )



class matchClassView(View):
    def get(self, request, *args, **kwargs):
        balls = BallDetails.objects.filter(season_id = kwargs.get('id')).values()
        print(balls)
        return render(
            request,
            template_name = 'matchDetails.html',
             context = {
                'title' : "MatchInfo",
                'balls' : balls,
            }
        )