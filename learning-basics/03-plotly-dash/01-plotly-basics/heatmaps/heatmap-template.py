import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df1 = pd.read_csv("2010SantaBarbaraCA.csv")
df2 = pd.read_csv("2010SitkaAK.csv")
df3 = pd.read_csv("2010YumaAZ.csv")

trace0 = go.Heatmap(
    x=df1["DAY"],
    y=df1["LST_TIME"],
    z=df1["T_HR_AVG"].values.tolist(),
    colorscale="jet",
    colorbar=dict(title="(ºC)"),
    zmin=5,
    zmax=40,
)

trace1 = go.Heatmap(
    x=df2["DAY"],
    y=df2["LST_TIME"],
    z=df2["T_HR_AVG"].values.tolist(),
    colorscale="jet",
    colorbar=dict(title="(ºC)"),
    zmin=5,
    zmax=40,
)

trace2 = go.Heatmap(
    x=df3["DAY"],
    y=df3["LST_TIME"],
    z=df3["T_HR_AVG"].values.tolist(),
    colorscale="jet",
    colorbar=dict(title="(ºC)"),
    zmin=5,
    zmax=40,
)

fig = make_subplots(
    rows=1,
    cols=3,
    subplot_titles=("Santa Barbara", "Sitka", "Yuma"),
)

fig.add_trace(trace0, 1, 1)
fig.add_trace(trace1, 1, 2)
fig.add_trace(trace2, 1, 3)
fig.update_layout(
    title="Temperatures in 3 cities",
    xaxis_title="Day of the week",
    yaxis_title="Hour of the day",
)

pyo.plot(fig, filename="heatmap-template.html", auto_open=False)
