import requests
from datetime import date

def get_current_game():
    # balldontlie API URL
    base_url = "https://www.balldontlie.io/api/v1/games?team_ids[]=25"
    today = date.today()
    req_url = base_url + "&start_date=" + today + "&end_date=" + today
    game_data = requests.get(req_url)
    if game_data:
        return game_data.home_team_score
    return

