import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("iris.csv")

trace0 = df[df["class"] == "Iris-setosa"]["sepal_length"]
trace1 = df[df["class"] == "Iris-versicolor"]["sepal_length"]
trace2 = df[df["class"] == "Iris-virginica"]["sepal_length"]

hist_data = [trace0, trace1, trace2]
group_labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.1, 0.1])

pyo.plot(fig, filename="iris-distplot.html", auto_open=False)
