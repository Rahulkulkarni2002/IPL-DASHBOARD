import polars as pl

def load_data(path):
    return pl.read_csv(path, ignore_errors=True)

def top_batsmen(df, top_n=10):
    return df.group_by("batter").agg(pl.col("runs_batter").sum().alias("total_runs")).sort("total_runs", descending=True).head(top_n)

def strike_rate(df, min_balls=500):
    return df.group_by("batter").agg([pl.col("runs_batter").sum().alias("total_runs"), pl.col("balls_faced").sum().alias("total_balls")]).with_columns((pl.col("total_runs") / pl.col("total_balls") * 100).alias("strike_rate")).filter(pl.col("total_balls") >= min_balls).sort("strike_rate", descending=True)

def boundaries(df, top_n=10):
    return df.filter((pl.col("runs_batter").is_in([4, 6])) & (pl.col("runs_not_boundary") == False)).group_by("batter").agg([(pl.col("runs_batter") == 4).sum().alias("fours"), (pl.col("runs_batter") == 6).sum().alias("sixes")]).with_columns((pl.col("fours") + pl.col("sixes")).alias("total_boundaries")).sort("total_boundaries", descending=True).head(top_n)

def top_bowlers(df, top_n=10, min_balls=300):
    return df.group_by("bowler").agg([pl.col("bowler_wicket").sum().alias("total_wickets"), pl.col("runs_bowler").sum().alias("total_runs"), pl.col("valid_ball").sum().alias("total_balls")]).with_columns([(pl.col("total_runs") / pl.col("total_balls") * 6).alias("economy_rate"), (pl.col("total_balls") / pl.col("total_wickets")).alias("bowling_strike_rate")]).filter(pl.col("total_balls") >= min_balls).sort("total_wickets", descending=True).head(top_n)

def top_catchers(df, top_n=10):
    return df.filter(pl.col("wicket_kind") == "caught").group_by("fielders").agg(pl.len().alias("catches")).sort("catches", descending=True).head(top_n)

def team_wins(df):
    return df.group_by("match_won_by").agg(pl.len().alias("wins")).sort("wins", descending=True)

def toss_impact(df):
    return df.with_columns((pl.col("toss_winner") == pl.col("match_won_by")).alias("toss_win_match_win")).group_by("toss_win_match_win").agg(pl.len().alias("count"))

def season_trends(df):
    return df.group_by("season").agg([pl.col("runs_total").sum().alias("total_runs"), pl.col("match_id").n_unique().alias("total_matches")]).with_columns((pl.col("total_runs") / pl.col("total_matches")).alias("avg_runs_per_match")).sort("season")

def sixes_per_season(df):
    return df.filter((pl.col("runs_batter") == 6) & (pl.col("runs_not_boundary") == False)).group_by("season").agg(pl.len().alias("total_sixes")).sort("season")

def top_batsman_per_season(df):
    return df.group_by(["season", "batter"]).agg(pl.col("runs_batter").sum().alias("runs")).sort(["season", "runs"], descending=[False, True]).group_by("season").first().sort("season")
