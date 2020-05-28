#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


timesData = pd.read_csv("data/timesData.csv")
df2011 = timesData[timesData.year == 2011].iloc[:50,:]
df2012 = timesData[timesData.year == 2012].iloc[:50,:]


layout1 = html.Div([
    dcc.Graph(
        id='plot2011',
        figure={
            'data': [
                go.Scatter(
                    x=df2011[df2011['country'] == i]['female_male_ratio'],
                    y=df2011[df2011['country'] == i]['num_students'],
                    text=df2011[df2011['country'] == i]['university_name'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df2011.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0.0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    html.Div(id='id2011'),
    dcc.Link('Go to App 2012', href='/apps/2012')
])


layout2 = html.Div([
    dcc.Graph(
        id='plot2012',
        figure={
            'data': [
                go.Scatter(
                    x=df2012[df2012['country'] == i]['female_male_ratio'],
                    y=df2012[df2012['country'] == i]['num_students'],
                    text=df2012[df2012['country'] == i]['university_name'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df2012.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0.0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    html.Div(id='id2012'),
    dcc.Link('Go to App 2011', href='/apps/2011')
])


