#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output

from app import app

@app.callback(
    Output('id2011', 'children'),
    [Input('plot2011', 'value')])

def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('id2012', 'children'),
    [Input('plot2012', 'value')])

def display_value(value):
    return 'You have display"{}"'.format(value)