import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

csv = pd.read_csv("2010YumaAZ.csv")
days = ["TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", "MONDAY"]

df = csv[["DAY", "LST_TIME", "T_HR_AVG"]]

data = []

for day in days:
    trace = go.Scatter(
        x=df[df["DAY"] == day]["LST_TIME"],
        y=df[df["DAY"] == day]["T_HR_AVG"],
        mode="lines",
        name=day,
    )
    data.append(trace)

layout = go.Layout(
    xaxis_title="Time (24h)",
    yaxis_title="Temperature (ºC)",
    legend_title="Days",
    title="Average Temperature Over The Days",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(
    fig,
    filename="2010YumaAZ-line-charts.html",
    auto_open=False,
)
