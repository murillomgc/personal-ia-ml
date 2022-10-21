import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("abalone.csv")

data = [go.Histogram(x=df["length"], xbins=dict(start=0, end=1, size=0.02))]
layout = go.Layout(
    title="Histogram of Length of Abalones",
    xaxis=dict(title="Length"),
    yaxis=dict(title="Count"),
)
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="abalone-histogram.html", auto_open=False)
