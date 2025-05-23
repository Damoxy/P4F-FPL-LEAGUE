import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env automatically

LEAGUE_ID = os.getenv("LEAGUE_ID")

FPL_LEAGUE_URL = f"https://fantasy.premierleague.com/api/leagues-classic/{LEAGUE_ID}/standings/"
FPL_FIXTURES_URL = "https://fantasy.premierleague.com/api/fixtures/"
