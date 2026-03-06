import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(

    style={"backgroundColor": "#f4f4f4", "padding": "30px"},

    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            children=[

                html.Label(
                    "Select Region:",
                    style={"fontSize": "20px", "fontWeight": "bold"}
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "20px"}
                ),

                dcc.Graph(id="sales-chart")

            ],
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0px 0px 10px rgba(0,0,0,0.1)"
            }
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    filtered_df = filtered_df.groupby("date").sum().reset_index()

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
