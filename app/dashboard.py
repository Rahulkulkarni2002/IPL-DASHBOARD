import streamlit as st
import polars as pl
import plotly.express as px
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))
from analysis import *

st.set_page_config(page_title="IPL Analytics Dashboard", page_icon="🏏", layout="wide")


@st.cache_data
def load():
    data_path = os.path.join(os.path.dirname(__file__), "../data/IPL.csv")
    return load_data(data_path)


df = load()

st.title("IPL Analytics Dashboard")
st.markdown("Ball-by-ball analysis of IPL 2008-2025")

seasons = sorted(df["season"].unique().to_list())
selected_season = st.sidebar.selectbox("Select Season", ["All"] + seasons)

if selected_season != "All":
    df = df.filter(pl.col("season") == selected_season)

st.markdown("---")
st.header("Batting Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Run Scorers")
    bat_df = top_batsmen(df).to_pandas()
    fig = px.bar(
        bat_df,
        x="total_runs",
        y="batter",
        orientation="h",
        color="total_runs",
        color_continuous_scale="Blues",
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Best Strike Rates (min 500 balls)")
    sr_df = strike_rate(df).head(10).to_pandas()
    fig2 = px.bar(
        sr_df,
        x="strike_rate",
        y="batter",
        orientation="h",
        color="strike_rate",
        color_continuous_scale="Greens",
    )
    fig2.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Most Boundaries")
    b_df = boundaries(df).to_pandas()
    fig3 = px.bar(
        b_df,
        x="batter",
        y=["fours", "sixes"],
        barmode="stack",
        color_discrete_map={"fours": "#3498db", "sixes": "#e74c3c"},
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Top Catchers")
    c_df = top_catchers(df).to_pandas()
    fig4 = px.bar(
        c_df,
        x="catches",
        y="fielders",
        orientation="h",
        color="catches",
        color_continuous_scale="Purples",
    )
    fig4.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.header("Bowling Analysis")
col5, col6 = st.columns(2)

with col5:
    st.subheader("Top 10 Wicket Takers")
    bowl_df = top_bowlers(df).to_pandas()
    fig5 = px.bar(
        bowl_df,
        x="total_wickets",
        y="bowler",
        orientation="h",
        color="total_wickets",
        color_continuous_scale="Reds",
    )
    fig5.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("Best Economy Rates (min 300 balls)")
    eco_df = top_bowlers(df).sort("economy_rate").head(10).to_pandas()
    fig6 = px.bar(
        eco_df,
        x="economy_rate",
        y="bowler",
        orientation="h",
        color="economy_rate",
        color_continuous_scale="Oranges",
    )
    fig6.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.header("Team Analysis")
col7, col8 = st.columns(2)

with col7:
    st.subheader("Team Wins")
    tw_df = team_wins(df).to_pandas()
    fig7 = px.bar(
        tw_df,
        x="wins",
        y="match_won_by",
        orientation="h",
        color="wins",
        color_continuous_scale="Teal",
    )
    fig7.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig7, use_container_width=True)

with col8:
    st.subheader("Toss Impact on Match Result")
    toss_df = toss_impact(df).to_pandas()
    toss_df["label"] = toss_df["toss_win_match_win"].map(
        {True: "Won Toss & Match", False: "Won Toss, Lost Match"}
    )
    fig8 = px.pie(
        toss_df,
        values="count",
        names="label",
        color_discrete_map={
            "Won Toss & Match": "#2ecc71",
            "Won Toss, Lost Match": "#e74c3c",
        },
    )
    st.plotly_chart(fig8, use_container_width=True)

st.markdown("---")
st.header("Season Trends")
col9, col10 = st.columns(2)

with col9:
    st.subheader("Average Runs Per Match by Season")
    st_df = season_trends(df).to_pandas()
    fig9 = px.line(
        st_df,
        x="season",
        y="avg_runs_per_match",
        markers=True,
        color_discrete_sequence=["#3498db"],
    )
    st.plotly_chart(fig9, use_container_width=True)

with col10:
    st.subheader("Total Sixes Per Season")
    six_df = sixes_per_season(df).to_pandas()
    fig10 = px.bar(
        six_df,
        x="season",
        y="total_sixes",
        color="total_sixes",
        color_continuous_scale="Reds",
    )
    st.plotly_chart(fig10, use_container_width=True)

st.markdown("---")
st.markdown(
    "Analyzing 17 seasons of IPL ball-by-ball data (2008-2025) to uncover player performance trends, team dominance, and how the game has evolved over time. Built with Python, Polars, and Streamlit by Rahul Kulkarni"
)
