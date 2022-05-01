# -*- coding: utf-8 -*-
"""
@author: NEEL SHAH
"""
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'D:\NSII\FSI-MAVs\HeatMapTry.csv')
df = df.pivot("Birds", "Winglength", "ReynoldsNumber")
    
fig = px.imshow(df,color_continuous_scale = px.colors.sequential.thermal,title = "Title can be decided soon")
fig.update_layout(title_font = {'size':27}, title_x = 0.5)
fig.update_traces(hoverongaps = False)
fig.show()
