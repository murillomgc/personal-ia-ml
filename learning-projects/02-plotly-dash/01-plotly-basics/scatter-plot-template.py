import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

rand_x = np.random.randint(1, 101, 100)
rand_y = np.random.randint(1, 101, 100)

trace = [
    go.Scatter(
        x=rand_x,
        y=rand_y,
        mode="markers",
        marker=dict(size=10, color="rgb(255,0,0)", symbol="x", line={"width": 1}),
    )
]

layout = go.Layout(
    title="Scatter Plot",
    xaxis={"title": "X"},
    yaxis={"title": "Y"},
    hovermode="closest",
)

fig = go.Figure(data=trace, layout=layout)

pyo.plot(fig, filename="scatter-plot-template.html", auto_open=False)
