import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd


app = dash.Dash()

df = pd.read_csv("OldFaithful.csv")

# Create a Dash layout that contains a Graph component:

app.layout = html.Div(
    [
        dcc.Graph(
            id="scatterplot",
            figure={
                "data": [
                    go.Scatter(
                        x=df["X"],
                        y=df["Y"],
                        mode="markers",
                        marker={
                            "size": 8,
                            "color": "#ff0000",
                            "symbol": "circle",
                            "line": {"width": 1},
                        },
                    )
                ],
                "layout": go.Layout(
                    title="Old Faithful Geyser Data",
                    xaxis={"title": "Eruptions Time (minutes)"},
                    yaxis={"title": "Waiting Time (minutes)"},
                ),
            },
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
