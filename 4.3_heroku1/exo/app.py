#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2('Bonjour'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['TMI', 'BBA', 'GPGE', 'TEF', 'CI']], # Taj Mahal Inde
                                                                                         # Big Ben Angleterre
                                                                                         # Grande Pyramide de Gizeh Egypte
                                                                                         # Tour Eiffel France
                                                                                         # Le Colisée Italie
        value='TMI'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])

def display_value(value):
    return 'Vous avez selectionnez "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)

