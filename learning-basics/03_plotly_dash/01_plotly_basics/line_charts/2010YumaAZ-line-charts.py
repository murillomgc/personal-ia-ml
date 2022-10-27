import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

csv = pd.read_csv("2010YumaAZ.csv")
df = csv[["DAY", "LST_TIME", "T_HR_AVG"]]

data = []

data = [
    {"x": df["LST_TIME"], "y": df[df["DAY"] == day["T_HR_AVG"]]}
    for day in df["DAY"].unique()
]

layout = go.Layout(
    xaxis_title="Time (24h)",
    yaxis_title="Temperature (ºC)",
    legend_title="Days",
    title="Average Temperature Over The Days",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(
    fig,
    filename="2010YumaAZ.html",
    auto_open=False,
)
