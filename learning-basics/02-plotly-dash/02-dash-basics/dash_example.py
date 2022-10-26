import dash
from dash import dcc
from dash import html


app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1("Hello Dash!"),
        html.Div("Dash: A web application framework for Python."),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {"x": [1, 2, 3], "y": [2, 4, 6], "type": "bar", "name": "NYC"},
                ],
                "layout": {"title": "Dash Data Visualization"},
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server()
