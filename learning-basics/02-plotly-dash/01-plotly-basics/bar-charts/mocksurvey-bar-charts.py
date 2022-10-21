import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

df = pd.read_csv("mocksurvey.csv", index_col=0)

data = [
    go.Bar(y=df.index, x=df[answer], name=answer, orientation="h")
    for answer in df.columns
]

layout = go.Layout(
    title="Survey Results",
    xaxis={"title": "Answer"},
    yaxis={"title": "Number of Responses"},
    legend_title="Answers",
    barmode="stack",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="mocksurvey.html", auto_open=False)
