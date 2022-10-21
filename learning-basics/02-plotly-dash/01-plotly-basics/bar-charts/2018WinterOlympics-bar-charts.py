import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv("2018WinterOlympics.csv")

trace0 = go.Bar(x=df["NOC"], y=df["Total"], name="Total", marker={"color": "#cf0e0e"})
trace1 = go.Bar(x=df["NOC"], y=df["Gold"], name="Gold", marker={"color": "#ffbb00"})
trace2 = go.Bar(x=df["NOC"], y=df["Silver"], name="Silver", marker={"color": "#808080"})
trace3 = go.Bar(x=df["NOC"], y=df["Bronze"], name="Bronze", marker={"color": "#af6b28"})

data = [trace1, trace2, trace3]

layout = go.Layout(
    title="2018 Winter Olympics Medals by Country",
    xaxis={"title": "Country"},
    yaxis={"title": "Number of Medals"},
    legend_title="Medals Type",
    barmode="stack",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="2018WinterOlympics.html", auto_open=False)
