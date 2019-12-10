################################################################################################
#### Dash application of Team 2 - Bogotá - DS4A
################################################################################################

# Load main libraries
from plotly import tools as pytools
import plotly_express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
# import functional libraries

from datetime import datetime as dt
import pandas as pd
####################################################################
#Import dataframes
####################################################################

####################################################################
### SQL conector
####################################################################
import psycopg2
engine = psycopg2.connect(
    database="final_db",
    user="juan",
    password="1234",
    host="nps-demo-instance.c2fezqs1nmx5.us-east-2.rds.amazonaws.com",
    port='5432'
)

layout = html.Div(children=[
    html.Br(),
    html.Br(),
    html.Br(), 
    html.H4("Landing:"),
    html.Div([
       
    
    html.Div([html.H4("Selector de Fecha:"),
        dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(2010, 1, 1),
        max_date_allowed=dt(2019, 11, 15),
        start_date =dt(2019, 1, 1),
        end_date=dt(2019, 8, 25)
    )],style={ 'width': '25%','float': 'left', 'display': 'inline-block',"padding-left":"5%"} ),
    
    html.Div([html.H4("Región:"),
        dcc.Dropdown(
                    id='fase-dropdown-rnfs',
                     )],
    style={ 'width': '25%','float': 'left', 'display': 'inline-block',"padding-left":"5%"}),
    html.Div([html.H4("Entidad:"),
        dcc.Dropdown(
            id='entidad-dropdown',
        )
    ],style={ 'width': '25%','float': 'left', 'display': 'inline-block',"padding-left":"5%"}),    
    ]),
    html.Div([],)
])

###############################################################################################
# Callback de lista de regiones disponibles
###############################################################################################
@app.callback(Output('fase-dropdown-rnfs', 'options'),
[Input('my-date-picker-range', 'start_date'),
 Input('my-date-picker-range', 'end_date'),])
def Update_RegionDropdown(Start_date,End_date):
    sql3 = """
    SELECT departamento_entidad
    FROM secopi
    where fecha_de_firma_del_contrato = '20/04/2017'
    limit 100
    """
    print(sql3)
    regions = pd.read_sql(sql3, con=engine)
    #print(regions)
    regions=regions["departamento_entidad"].unique()
    
    return [{'label': i, 'value': i}
            for i in regions]
################################################################################
# Callback to update the posible values of animal dropdown list
################################################################################
@app.callback(
    Output('fase-dropdown-rnfs', 'value'),
    [Input('fase-dropdown-rnfs', 'options')])
def update_RegionDropdown_value(region_seleccionada):
    """updates the region dropdown value"""
    return region_seleccionada[0]['value'] 


###############################################################################################
# Callback de lista de entidades disponibles
###############################################################################################
@app.callback(Output('entidad-dropdown', 'options'),
[Input('fase-dropdown-rnfs', 'value'),])
def Update_EntidadDropdown(region='Casare'):
    sql4 = """
    SELECT  nombre_de_la_entidad
    FROM secopi
    where departamento_entidad ='{}'
    limit 100
    """.format(region)
    entidades = pd.read_sql(sql4, con=engine)
    #engine.close()
    #print(sql4)
    #print(entidades)
    entidades=entidades["nombre_de_la_entidad"].unique()
    
    return [{'label': i, 'value': i}
            for i in entidades]
################################################################################
# Callback to update the posible values of animal dropdown list
################################################################################
@app.callback(
    Output('entidad-dropdown', 'value'),
    [Input('entidad-dropdown', 'options')])
def update_entidadDropdown_value(entidad_seleccionada):
    """updates the entidad dropdown value"""
    return entidad_seleccionada[0]['value'] 