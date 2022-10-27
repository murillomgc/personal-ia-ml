import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv("gapminderDataFiveYear.csv")

year_options = []
for year in df["year"].unique():
    year_options.append({"label": str(year), "value": year})


app = dash.Dash()
app.layout = html.Div(
    [
        dcc.Graph(id="graph"),
        dcc.Dropdown(
            id="year-picker",
            options=year_options,
            value=df["year"].min(),
        ),
    ]
)


@app.callback(Output("graph", "figure"), [Input("year-picker", "value")])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    traces = []
    for continent_name in filtered_df["continent"].unique():
        df_by_continent = filtered_df[filtered_df["continent"] == continent_name]
        traces.append(
            go.Scatter(
                x=df_by_continent["gdpPercap"],
                y=df_by_continent["lifeExp"],
                mode="markers",
                marker={"size": 15},
                opacity=0.7,
                text=df_by_continent["country"],
                name=continent_name,
            )
        )

    return {
        "data": traces,
        "layout": go.Layout(
            title="Interactive Plot - Life Expectancy vs. GDP per Capita",
            xaxis={"title": "GDP Per Capita", "type": "log"},
            yaxis={"title": "Life Expectancy"},
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=True)
