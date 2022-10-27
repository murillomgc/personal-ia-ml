import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(50) - 3
x2 = np.random.randn(500)
x3 = np.random.randn(5000) + 3
x4 = np.random.randn(50000) + 6

hist_data = [x1, x2, x3, x4]
group_labels = ["50 Samples", "500 Samples", "5k Samples", "50k Samples"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.1, 0.1, 0.1])

pyo.plot(fig, filename="distribuition-plot-template.html", auto_open=False)
