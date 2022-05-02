# -*- coding: utf-8 -*-
"""
@author: NEEL SHAH
"""
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'D:\NSII\FSI-MAVs\HeatMapTry.csv')
df = df.pivot("Birds", "Winglength", "ReynoldsNumber")
    
fig = px.imshow(df,color_continuous_scale = px.colors.sequential.Plasma,title = "Winglength v/s Reynolds Number")
fig.update_layout(title_font = {'size':27}, title_x = 0.5)

fig.update_traces(hoverongaps = False, 
                 hovertemplate = "Winglength: %{y}"
                                 "<br> Winglength: %{x}"
                                 "<br> Reynolds Number: %{z}<extra></extra>")
fig.show()
