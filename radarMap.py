# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:17:42 2022

@author: NEEL SHAH
"""


import pandas as pd
import plotly.express as px

#df = pd.read_csv(r'fILE PATH\FinalCSV.csv')
df = pd.read_csv(r'D:\NSII\FSI-MAVs\FinalCSV.csv')

df = pd.melt(df,id_vars=['PARAMETERS'],var_name='Birds', value_name='Value', 
             value_vars = ['Chickadee','Hoopoe','Tern','Pigeon','Lark','Finch','Magpie'], )


fig = px.line_polar(df, r='Value', theta='Birds', color='PARAMETERS',line_close=(True),
                    line_shape='linear',hover_name='PARAMETERS',hover_data = {'PARAMETERS':False},
                    markers=(True), direction='clockwise',start_angle=45)

fig.update_traces(fill = 'toself')
                    
fig.show()

