import json
from datetime import datetime
import pytz

import requests
import urllib3
urllib3.disable_warnings()

url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

response = requests.get(url, verify=False)
JSON = response.json()

class TeamData:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name

# print(JSON)
for event in JSON["events"]:
    teams = event["name"].split(" at ")

    # Convert the timestamp string to a datetime object
    timestamp_utc = datetime.fromisoformat(event["date"])

    # Define the UTC timezone
    utc_timezone = pytz.utc

    # Convert the UTC datetime object to Eastern Standard Time (EST)
    est_timezone = pytz.timezone('US/Eastern')
    timestamp_est = timestamp_utc.astimezone(est_timezone)

    # Convert the EST datetime object to a string
    formatted_timestamp = timestamp_est.strftime("%Y-%m-%d %H:%M:%S %Z")

    print(formatted_timestamp)

    print(teams[0] + " vs. " + teams[1])
    print("@", event["competitions"][0]["venue"]["fullName"] + ". \nThe final score is: \n" + event["competitions"][0]["competitors"][1]["score"], "to", event["competitions"][0]["competitors"][0]["score"])

    # for some reason the scores are flipped
    team1 = TeamData(teams[0], event["competitions"][0]["competitors"][1]["score"])
    team2 = TeamData(teams[1], event["competitions"][0]["competitors"][0]["score"])

    #compare scores in a tuple
    game_score_tuple = (team1, team2)

    if int(team1.score) == 0 and int(team2.score) == 0:
        print("Game is delayed or abandoned \n\n" )

    elif int(team1.score) > int(team2.score):
        print(team1, "win \n\n")

    else:
        print(team2, "win \n\n")

    # print(team1, team1.score)


# print(JSON["events"][0])