import pandas as pd
import csv
import plotly.graph_objects as pgo
df=pd.read_csv('class-105.csv')
student2=df.loc[df['student_id']=='TRL_xyz']
print(student2.groupby('level')['attempt'].mean())
figure2=pgo.Figure(pgo.Bar(
    x=student2.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'
))
figure2.show()