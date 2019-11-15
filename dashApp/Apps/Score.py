from plotly import tools as pytools
import plotly_express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
####################################################################
#Import dataframes
####################################################################


layout = html.Div(children=[
    html.Br(),
    html.Br(),
    html.Br(), 
    html.H4("Análisis de variabilidad"),
    html.Div([
       
    html.H4(" Variable de interés"),
    dcc.Dropdown(
                    id='fase-dropdown-rnfs',
                     options=[
                        {
                            "label": 'Mortalidad (%)',
                            "value": 'mortalidadPor'
                        },
                        {
                            "label": 'Ganancia diaria Promedio',
                            "value": 'gad'
                        },
                        {
                            "label": 'Peso Final Promedio',
                            "value": 'Peso'
                        },
                        {
                            "label": 'Consumo animal día promedio',
                            "value": 'cad'
                        },
                        {
                            "label": 'Conversión',
                            "value": 'conv'
                        },
                     ],
                    value="Peso"),
    ], style={ 'width': '50%','float': 'left', 'display': 'inline-block',"padding-left":"5%"}),    
    
    

])
