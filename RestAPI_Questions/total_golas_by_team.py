"""
✅ Question 1: REST API – Total Goals by a Team
Problem Statement:

In this challenge, the REST API contains information about football matches.
You are provided with an API that allows querying matches by teams and year.
Your task is to get the total number of goals scored by a given team in a given year.

API Details:

To access a collection of matches, use:

php-template
Copy
Edit
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team2=<team>&page=<page>
Where:

year = year of the competition.

team1 = home team name.

team2 = away team name.

page = page number (pagination starts from 1).

Response Structure Example:

json
Copy
Edit
{
    "page": 1,
    "per_page": 10,
    "total": 20,
    "total_pages": 2,
    "data": [
        {
            "competition": "UEFA Champions League",
            "year": 2011,
            "team1": "Barcelona",
            "team2": "Real Madrid",
            "team1goals": "3",
            "team2goals": "1"
        }
    ]
}
Function Signature:

python
Copy
Edit
def getTotalGoals(team: str, year: int) -> int
Input:

team (string): name of the team.

year (integer): year of the matches.

Output:

Return an integer: total goals scored by the team in that yea
"""





#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests


def getTotalGoals(team, year):
    total_goals = 0

    def fetch_goals(param_name):
        nonlocal total_goals
        page = 1
        while True:
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&{param_name}={team}&page={page}"

            response = requests.get(url).json()
            data = response.get("data", [])

            for match in data:
                if param_name == "team1":
                    total_goals += int(match["team1goals"])
                if param_name == "team2":
                    total_goals += int(match["team2goals"])
            if page >= response.get("total_pages", 0):
                break
            page += 1

    # Fetch for home team
    fetch_goals("team1")
    # Fetch for away team
    fetch_goals("team2")

    return total_goals

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
