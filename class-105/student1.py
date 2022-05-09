import pandas as pd
import csv
import plotly.graph_objects as pgo
df=pd.read_csv('class-105.csv')
student1=df.loc[df['student_id']=='TRL_zet']
print(student1.groupby('level')['attempt'].mean())
figure1=pgo.Figure(pgo.Bar(
    x=student1.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'
))
figure1.show()