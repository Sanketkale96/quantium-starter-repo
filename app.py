import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("formatted_sales.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Group sales by date
df = df.groupby("date").sum().reset_index()

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Soul Foods Pink Morsel Sales Dashboard"),

    dcc.Graph(figure=fig)

])

if __name__ == "__main__":
    app.run(debug=True)
