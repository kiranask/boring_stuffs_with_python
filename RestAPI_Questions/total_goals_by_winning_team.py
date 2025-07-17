"""
✅ Question 2: REST API – Football Competition Winner's Goals
Problem Statement:

In this challenge, the REST API contains information about football competitions and matches.
The API allows querying competitions by name and year.
Your task is:
For a given competition name and year, get the total number of goals scored by the team that won the competition.

Step 1: Get Winner Team

Use the API:

php-template
Copy
Edit
https://jsonmock.hackerrank.com/api/football_competitions?name=<competition>&year=<year>
Example Response:

json
Copy
Edit
{
    "page": 1,
    "per_page": 10,
    "total": 1,
    "total_pages": 1,
    "data": [
        {
            "name": "UEFA Champions League",
            "country": "Europe",
            "year": 2011,
            "winner": "Barcelona",
            "runnerup": "Manchester United"
        }
    ]
}
Step 2: Get Goals Scored by Winner

Use the same matches API as Question 1, but filter by:

year = <year>

team1 = <winner_team> and team2 = <winner_team>

Important: Count only matches where competition == given competition.

Function Signature:

python
Copy
Edit
def getWinnerTotalGoals(competition: str, year: int) -> int
Input:

competition (string): name of the competition.

year (integer): year of the competition.

Output:

Return an integer: total goals scored by the winning team in that competition for that year.

Do you want me to give the exact HackerRank-style prompt with examples and constraints for both, so you can use them for practice or interviews?
Or prepare test cases with expected outputs for both problems?
"""


#!/bin/python3

import os
import sys
import requests
import urllib.parse

def getWinnerTotalGoals(competition, year):
    comp_enc = urllib.parse.quote(competition)

    # Step 1: get competition details
    comp_url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={comp_enc}&year={year}"
    resp = requests.get(comp_url).json()
    data = resp.get("data", [])
    if not data:
        return 0

    winner_team_raw = data[0]["winner"]
    winner_team_enc = urllib.parse.quote(winner_team_raw)

    total_goals = 0

    def fetch_total_goals(param_name):
        nonlocal total_goals
        page = 1
        while True:
            url = (
                f"https://jsonmock.hackerrank.com/api/football_matches"
                f"?year={year}&{param_name}={winner_team_enc}&page={page}"
            )
            res = requests.get(url).json()
            matches = res.get("data", [])
            for match in matches:
                # count ONLY matches from the requested competition
                if match.get("competition") != competition:
                    continue
                if param_name == "team1":
                    total_goals += int(match["team1goals"])
                else:
                    total_goals += int(match["team2goals"])
            if page >= res.get("total_pages", 0):
                break
            page += 1

    fetch_total_goals("team1")
    fetch_total_goals("team2")

    return total_goals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    competition = input().strip()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    fptr.write(str(result) + '\n')
    fptr.close()
