from django.db import models

# Create your models here.
from django.db import models



class seasons(models.Model):
    match_id = models.IntegerField(primary_key= True)
    season = models.IntegerField()
    city = models.CharField(max_length = 256)
    date = models.CharField(max_length = 256)
    team1 = models.CharField(max_length = 256)
    team2 = models.CharField(max_length = 256)
    toss_winner = models.CharField(max_length = 256)
    toss_decision = models.CharField(max_length = 256)
    result = models.CharField(max_length = 256)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length = 256)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length = 256)
    venue = models.CharField(max_length = 256)
    umpire1 = models.CharField(max_length = 256, blank = True, null = True)
    umpire2 = models.CharField(max_length = 256, blank = True, null = True)
    umpire3 = models.CharField(max_length = 256, blank = True, null = True)

    def __int__(self):
        return self.season

class BallDetails(models.Model):
    season_id = models.ForeignKey(seasons, on_delete = models.CASCADE)
    innings = models.IntegerField()
    batting_team = models.CharField(max_length = 256)
    bowling_team = models.CharField(max_length = 256)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length = 256)
    non_striker = models.CharField(max_length = 256)
    bowler = models.CharField(max_length = 256)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length = 256)
    dismissal_kind = models.CharField(max_length = 256)
    fielder = models.CharField(max_length = 256)



