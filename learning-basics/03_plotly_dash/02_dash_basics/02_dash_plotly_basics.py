import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import numpy as np


app = dash.Dash()

# Creating random data
np.random.seed(42)
rand_x = np.random.randint(1, 101, 100)
rand_y = np.random.randint(1, 101, 100)
rand_xx = np.random.randint(1, 101, 100)
rand_yy = np.random.randint(1, 101, 100)

app.layout = html.Div(
    [
        dcc.Graph(
            id="scatterplot",
            figure={
                "data": [
                    go.Scatter(
                        x=rand_x,
                        y=rand_y,
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
                    title="Scatterplot (Random Data)",
                    xaxis={"title": "Random X"},
                    yaxis={"title": "Random Y"},
                ),
            },
        ),
        dcc.Graph(
            id="scatterplot2",
            figure={
                "data": [
                    go.Scatter(
                        x=rand_xx,
                        y=rand_yy,
                        mode="markers",
                        marker={
                            "size": 8,
                            "color": "#001aff",
                            "symbol": "circle",
                            "line": {"width": 1},
                        },
                    )
                ],
                "layout": go.Layout(
                    title="Scatterplot II (Random Data)",
                    xaxis={"title": "Random X"},
                    yaxis={"title": "Random Y"},
                ),
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
