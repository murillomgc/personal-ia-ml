import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

df = pd.read_csv("flights.csv")

data = [
    go.Heatmap(
        x=df["year"],
        y=df["month"],
        z=df["passengers"].values.tolist(),
        colorscale="Jet",
        colorbar=dict(title="Passengers"),
    )
]
layout = go.Layout(title="Flights", xaxis_title="Year", yaxis_title="Month")
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="flights-heatmap.html", auto_open=False)
