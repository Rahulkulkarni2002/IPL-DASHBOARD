# IPL Analytics Dashboard

An interactive analytics dashboard analyzing 17 seasons of IPL ball-by-ball data (2008–2025) to uncover player performance trends, team dominance, and how the game has evolved over time.

## What This Project Does

- Analyzes 280,000+ ball-by-ball records across 17 IPL seasons
- Identifies top batsmen, bowlers, and fielders by multiple metrics
- Tracks team win rates and toss impact on match outcomes
- Visualizes how scoring and six-hitting has evolved season by season
- Provides an interactive season filter to explore any specific IPL year

## Key Insights

- Top run scorers and best strike rates (min 500 balls faced)
- Most boundaries hit (fours and sixes separately)
- Top wicket takers and most economical bowlers (min 300 balls bowled)
- Most catches taken by fielders
- Team win rates across all seasons
- Whether winning the toss actually helps win the match
- Average runs per match and total sixes per season trend

## Tech Stack

- Python
- Polars — fast data manipulation (280K+ rows)
- Plotly — interactive charts
- Streamlit — web app deployment

## Project Structure
IPL-DASHBOARD/
├── app/
│   └── dashboard.py      # Streamlit web app
├── scripts/
│   └── analysis.py       # Analysis functions
├── data/                 # IPL dataset (not tracked - too large)
├── notebooks/            # EDA notebook
└── requirements.txt

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/Rahulkulkarni2002/IPL-DASHBOARD.git
cd IPL-DASHBOARD
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset from Kaggle:
https://www.kaggle.com/datasets/chaitu20/ipl-dataset2008-2025
Place the CSV file in the data/ folder.

4. Run the dashboard:
```bash
streamlit run app/dashboard.py
```

## Live Demo

Streamlit App Link — coming soon

## Author

Rahul Kulkarni | M.S. Business Analytics @ UC San Diego (Rady School of Management)

LinkedIn: https://www.linkedin.com/in/rahul-kulkarni-b3b067206
GitHub: https://github.com/Rahulkulkarni2002
