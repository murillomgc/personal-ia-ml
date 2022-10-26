import dash
from dash import dcc
from dash import html

app = dash.Dash()


app.layout = html.Div(
    [
        html.Label("Dropdown"),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "San Francisco", "value": "SF"},
                {"label": "Montreal", "value": "MTL"},
                {"label": "Los Angeles", "value": "LA"},
                {"label": "Ottawa", "value": "OTT"},
            ],
            value="NYC",
        ),
        html.Label("Slider"),
        dcc.Slider(min=-10, max=10, step=1, value=0),
        html.Label("Radio Items"),
        dcc.RadioItems(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "San Francisco", "value": "SF"},
                {"label": "Montreal", "value": "MTL"},
                {"label": "Los Angeles", "value": "LA"},
                {"label": "Ottawa", "value": "OTT"},
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
