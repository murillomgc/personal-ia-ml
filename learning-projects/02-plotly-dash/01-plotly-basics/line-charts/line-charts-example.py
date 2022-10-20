import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv("nst-est2017-alldata.csv")

df2 = df[df["DIVISION"] == "1"]
df2.set_index("NAME", inplace=True)

list_of_population_columns = [col for col in df2.columns if col.startswith("POP")]
df2 = df2[list_of_population_columns]

col_old_names = df2.columns.values
col_new_names = [year[11:] for year in (df2.columns.values)]
new_names_dict = dict(zip(col_old_names, col_new_names))
df2.rename(columns=new_names_dict, inplace=True)

data = [
    go.Scatter(x=df2.columns, y=df2.loc[name], mode="lines", name=name)
    for name in df2.index
]

layout = go.Layout(
    xaxis_title="Years",
    yaxis_title="Population",
    legend_title="Divisions",
    title="Estimated Population by Divisions",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(
    fig,
    filename="line-charts-example(nst-est2017-pop).html",
    auto_open=False,
)
