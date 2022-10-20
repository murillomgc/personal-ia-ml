import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)

values_x = np.linspace(0, 1, 100)
values_y = np.random.randn(100)

trace0 = go.Scatter(x=values_x, y=values_y + 5, mode="markers", name="markers")
trace1 = go.Scatter(x=values_x, y=values_y, mode="lines", name="lines")
trace2 = go.Scatter(
    x=values_x, y=values_y - 5, mode="lines+markers", name="lines+markers"
)

data = [trace0, trace1, trace2]

layout = go.Layout(title="Line Chart Examples")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="line-charts-template.html", auto_open=False)
