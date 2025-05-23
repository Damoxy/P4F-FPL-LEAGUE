from datetime import datetime
import pandas as pd

def map_gameweek_to_month(fixtures):
    gw_to_month = {}
    for fixture in fixtures:
        gw = fixture.get("event")
        date_str = fixture.get("kickoff_time")
        if gw and date_str:
            month = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%B")
            gw_to_month[gw] = month
    return gw_to_month

def aggregate_monthly_scores(managers, fetch_player_history_func, gw_to_month):
    monthly_scores = {}

    for manager in managers:
        manager_id = manager['entry']
        manager_name = manager['player_name']
        history = fetch_player_history_func(manager_id)

        if history and 'current' in history:
            for week in history['current']:
                gw = week['event']
                points = week['points']
                month = gw_to_month.get(gw, "Unknown")

                monthly_scores.setdefault(month, {})
                monthly_scores[month][manager_name] = monthly_scores[month].get(manager_name, 0) + points

    monthly_df = {month: pd.Series(scores) for month, scores in monthly_scores.items()}
    return pd.DataFrame(monthly_df).fillna(0)
