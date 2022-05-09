import pandas as pd
import csv 
import plotly.graph_objects as pgo
df=pd.read_csv('class-105.csv')
print(df.groupby('level')['attempt'].mean())
figure=pgo.Figure(pgo.Bar(
    x=df.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'

))
figure.show()