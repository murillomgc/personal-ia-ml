import dash
from dash import dcc
from dash import html


app = dash.Dash()

colors = {"background": "#111111", "text": "#7FDBFF"}


app.layout = html.Div(
    children=[
        html.H1("Hello Dash!", style={"textAlign": "center", "color": colors["text"]}),
        html.Div("Dash: A web application framework for Python."),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {"x": [1, 2, 3], "y": [2, 4, 6], "type": "bar", "name": "NYC"},
                ],
                "layout": {
                    "plot_bgcolor": colors["background"],
                    "paper_bgcolor": colors["background"],
                    "font": {"color": colors["text"]},
                    "title": "Dash Data Visualization",
                },
            },
        ),
    ],
    style={"backgroundColor": colors["background"]},
)


if __name__ == "__main__":
    app.run_server(debug=True)
