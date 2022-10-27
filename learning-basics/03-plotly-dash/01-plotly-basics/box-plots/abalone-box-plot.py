#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("abalone.csv")

sample_A = np.random.choice(df["rings"], 250, replace=False)
sample_B = np.random.choice(df["rings"], 250, replace=False)

data = [go.Box(y=sample_A, name="Sample A"), go.Box(y=sample_B, name="Sample B")]
layout = go.Layout(title="Two Random Samples of Abalone Rings")
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="abalone.html", auto_open=False)
