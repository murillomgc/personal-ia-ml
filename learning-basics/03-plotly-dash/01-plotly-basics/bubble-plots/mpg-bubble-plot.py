import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go


df = pd.read_csv("mpg.csv")

# Fixing csv database
df = df[df["horsepower"] != "?"]
df["horsepower"] = df["horsepower"].apply(pd.to_numeric)


data = [
    go.Scatter(
        x=df["horsepower"],
        y=df["mpg"],
        text=df["name"],
        mode="markers",
        marker=dict(
            size=df["weight"] / 150,
            color=df["cylinders"],
            colorscale="agsunset",
            showscale=True,
        ),
    )
]

layout = go.Layout(
    title="MPG vs Horsepower",
    hovermode="closest",
    xaxis_title="Horsepower",
    yaxis_title="MPG",
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="mpg.html", auto_open=False)
