#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table

timesData = pd.read_csv("data/timesData.csv")
df2011 = timesData[timesData.year == 2011]
df2012 = timesData[timesData.year == 2012]


def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT1sP7FJ94PEacbCJ1VXzRHA-TCuAiGT6e8LmMnZFgSWu9foCqg&usqp=CAU', height='101', width='141')
        ], className="ten columns padded"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Ranking of universities Report')
        ], className="twelve columns padded")

    ], className="row")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('2011      |     ', href='/apps/2011/', className="tab first"),

        dcc.Link('2012      |', href='/apps/2012', className="tab"),

    ], className="row")
    return menu


layout1 = html.Div([
    Header(),
    html.Div([   
        dash_table.DataTable(
            id='table2011',
            columns=[{"name": i, "id": i} for i in df2011.columns],
            data=df2011.to_dict('records'),
            editable=True,
            css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
            style_table={'overflowX': 'scroll',
                         'overflowY': 'scroll',
                         'width': '49%',
                         'Height' : '49%',
                         'display': 'inline-block',
                         'vertical-align': 'middle'},
            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#3C9900',
                    'color': 'white'
                }
            ],
            style_header={
                'backgroundColor': 'rgb(30, 30, 30)',
                'color' : 'white',
                'fontWeight': 'bold'
            },
    )]
    ),
    
    # Download Button
    html.Div([
          html.A(html.Button('Download Data', id='download-button'), id='download-data')
          ]),
    
    html.Div([  
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
    )]),
    html.Div(id='id2011'),
    dcc.Link('Go to App 2012', href='/apps/2012')
])


layout2 = html.Div([
    Header(),
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


