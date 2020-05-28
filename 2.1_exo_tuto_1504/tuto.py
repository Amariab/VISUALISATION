# FIRST CHART WITH DASH

# Import librairies :
import dash
import dash_core_components as dcc
import dash_html_components as html

print("tout est ok")

#  Application creation :
app = dash.Dash()
colors = {
    'background': '#663399',
    'text': '#FF3366'
}

# layout creation :
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children = 'Hello Dash',
        style = {
            'textAlign': 'center',
            'color': colors['text'] # line 14
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
  # graph creation :  
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
