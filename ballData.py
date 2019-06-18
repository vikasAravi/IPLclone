import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalHack.settings')
django.setup()
from IPLclone.models import *
import csv


def pullData():
    count = 0
    result = []
    with open('deliveries.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            object = BallDetails(
                season_id=seasons.objects.get(match_id=int(row['match_id'])),
                innings = int(row['inning']),
                batting_team = row['batting_team'],
                bowling_team = row['bowling_team'],
                over = int(row['over']),
                ball = int(row['ball']),
                batsman = row['batsman'],
                non_striker = row['non_striker'],
                bowler = row['bowler'],
                is_super_over = int(row['is_super_over']),
                wide_runs = int(row['wide_runs']),
                bye_runs = int(row['bye_runs']),
                legbye_runs = int(row['legbye_runs']),
                noball_runs = int(row['noball_runs']),
                penalty_runs = int(row['penalty_runs']),
                batsman_runs = int(row['batsman_runs']),
                extra_runs = int(row['extra_runs']),
                total_runs = int(row['total_runs']),
                player_dismissed = row['player_dismissed'],
                dismissal_kind = row['dismissal_kind'],
                fielder = row['fielder'],

            )
            count += 1
            result.append(object)
            print(count)
            if(count == 10000):
                BallDetails.objects.bulk_create(result)
                result = []
                count = 0
    BallDetails.objects.bulk_create(result)


if __name__ == "__main__":
    pullData()