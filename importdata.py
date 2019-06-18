import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalHack.settings')
django.setup()
from IPLclone.models import seasons
import csv


def pullData():
    count = 0
    with open('matches.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            match_id = row['id']
            if(match_id == None):
                continue
            season = row['season']
            city = row['city']
            date = row['date']
            team1 = row['team1']
            team2 = row['team2']
            toss_winner = row['toss_winner']
            toss_decision = row['toss_decision']
            result = row['result']
            dl_applied = bool(row['dl_applied'])
            winner = row['winner']
            win_by_runs = int(row['win_by_runs'])
            win_by_wickets = int(row['win_by_wickets'])
            player_of_match = row['player_of_match']
            venue = row['venue']
            umpire1 = row['umpire1']
            umpire2 = row['umpire2']
            umpire3 = row['umpire3']
            count += 1
            seasonObject = seasons(match_id = match_id, season = season, city = city, date = date, team1 = team1, team2 = team2, toss_winner = toss_winner, toss_decision = toss_decision, result = result, dl_applied = dl_applied, winner = winner, win_by_runs = win_by_runs, win_by_wickets = win_by_wickets, player_of_match = player_of_match, venue = venue, umpire1 = umpire1, umpire2 = umpire2, umpire3 = umpire3)
            print(count, seasonObject)
            seasonObject.save()



if __name__ == "__main__":
    pullData()