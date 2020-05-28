#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:13:57 2020

@author: Amariab
"""

"""Créer un dashboard Dash affichant un scatter plots avec le nombre 
d’étudiants total en fonction du Ratio étudiant féminin / étudiant masculin,
 pour les 20 premières université du classement."""
 
 
"""Create a dash dashboard displaying scatter plots with the number
of total students based on the female / male student ratio,
 for the top 20 universities in the ranking. """
 
# Librairies import
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
print("tout est ok")

# Application creation
app = dash.Dash()

# Data recovery
timesData = pd.read_csv("donnees/timesData.csv")
df = timesData.iloc[:20,:] # The top 20 universities

# Layout creation :

app.layout = html.Div([
    dcc.Graph(
        id="Etudiants et ratios mâle femelle",
        figure = {
            "data": [
                go.Scatter(
                    x=df["female_male_ratio"], # récupération des données
                    y=df["num_students"],
                    text = df["university_name"],
                    mode = "markers", # avec lines+markers : incompréhension
                    opacity = 0.8,
                    marker = {
                        "size": 25,
                        "color":"#0099FF",
                        "line": {"width": 5, "color": "black"}
                    }
                )
            ],
            "layout": go.Layout(
                xaxis = {"title": "Ratio mâle femelle"},
                yaxis = {"title": "nb total d'étudiants"},
                margin = {'l': 40, 'b': 40, 't': 10, 'r': 10, "pad" : 5},
                hovermode='closest',
                width = 1000,
                height= 500
            )
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)