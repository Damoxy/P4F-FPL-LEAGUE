import streamlit as st
import matplotlib.pyplot as plt

from fpl.config import LEAGUE_ID
from fpl.data_fetcher import fetch_league_standings, fetch_player_history, fetch_gameweek_dates
from fpl.data_processing import map_gameweek_to_month, aggregate_monthly_scores

def main():
    st.title("FPL Monthly League Standings")
    st.write("Fetching the data for League ID:", LEAGUE_ID)

    fixtures = fetch_gameweek_dates()
    gw_to_month = map_gameweek_to_month(fixtures)

    data = fetch_league_standings()
    if data:
        managers = data['standings']['results']
        monthly_df = aggregate_monthly_scores(managers, fetch_player_history, gw_to_month)

        st.dataframe(monthly_df)

        st.subheader("Top Scorers by Month")
        for month in monthly_df.columns:
            top_scorer = monthly_df[month].idxmax()
            top_points = monthly_df[month].max()
            st.write(f"**{month}:** {top_scorer} ({top_points} points)")

        st.subheader("Monthly Points Trend")
        monthly_df.T.plot(kind='bar', figsize=(12, 6))
        st.pyplot(plt)
    else:
        st.error("Failed to fetch league standings.")

if __name__ == "__main__":
    main()
