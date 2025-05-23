import requests
from config import FPL_LEAGUE_URL, FPL_FIXTURES_URL

def fetch_league_standings():
    response = requests.get(FPL_LEAGUE_URL)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_player_history(manager_id):
    url = f"https://fantasy.premierleague.com/api/entry/{manager_id}/history/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_gameweek_dates():
    response = requests.get(FPL_FIXTURES_URL)
    if response.status_code == 200:
        return response.json()
    return []
