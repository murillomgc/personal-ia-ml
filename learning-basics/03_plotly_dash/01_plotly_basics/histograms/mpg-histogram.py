import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("mpg.csv")

data = [go.Histogram(x=df["mpg"], xbins=dict(start=0, end=60, size=2))]
layout = go.Layout(
    title="Histogram of MPG", xaxis=dict(title="MPG"), yaxis=dict(title="Count")
)
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="mpg-histogram.html", auto_open=False)
