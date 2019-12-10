import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import datetime as dt
import datetime 


from app import app

####################################################################
#Import dataframes
####################################################################


list_departments_contratist = ['All', 'Amazonas', 'Antioquia', 'Arauca', 'Atlántico', 'Bogotá D.C.', 'Bolívar', 'Boyacá', 'Caldas', 'Caquetá', 'Casanare', 
                    'Cauca', 'Cesar', 'Chocó', 'Cundinamarca', 'Córdoba', 'Guainía', 'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta', 
                    'Nariño', 'Norte De Santander', 'Putumayo', 'Quindío', 'Risaralda', 'San Andrés, Providencia y Santa Catalina', 'Santander', 
                    'Sucre', 'Tolima', 'Valle del Cauca', 'Vaupés', 'Vichada']

list_nivel_contratist = ['All', 'Celebrado', 'Liquidado', 'Terminado sin Liquidar', 'Convocado',
       'Adjudicado', 'Terminado Anormalmente']

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


##################################################################

layout = html.Div(children=[
    html.Div(
        className="row app-body",
        children=[
            # User Controls
            html.Div(
                className="twelve columns",
                children=[
                    html.Div(
                        className="padding-top-bot row",
                        children=[
                            html.Div(
                                className="two columns",
                                children=[
                                    html.H6("Select Department",),
                                    dcc.Dropdown(
                                        id="department_dropdown_contratist",
                                        #multi=True,
                                        options = [{'label': i, 'value': i}
                                        for i in list_departments_contratist],                                            
                                        placeholder="Select department",
                                    ),
                                ]),
                                html.Div(
                                    className="two columns",
                                    children=[
                                        html.H6("Select Level"),
                                        dcc.Dropdown(
                                            id="level_dropdown_contratist",
                                            options = [{'label': i, 'value': i}
                                            for i in list_nivel_contratist],                                            
                                            #multi=True,
                                            placeholder="Select level",
                                    ),
                                ]),
                                html.Div(
                                    className='three columns',
                                    children=[
                                        html.H6("Select a Date Range"),
                                        dcc.DatePickerRange(
                                            id="date-range_contratist",
                                            min_date_allowed = dt(2013,1,1),
                                            max_date_allowed = dt(2019,12,31),
                                            display_format='DD MMM YYYY',
                                            start_date=dt(2019,7,1),
                                            end_date=dt(2019,12,31)
                                        ),
                                ]),
                                html.Div(
                                    id="Total_Amount_contratist_div",
                                    className="two columns indicator pretty_container",
                                    children=[
                                        html.P(id="Total_Amount_contratist", className="indicator_value"),
                                        html.P('Total Amount', className="twelve columns indicator_text"),
                                ]),
                                html.Div(
                                    id="Total_Quantity_contratist_div",
                                    className="two columns indicator pretty_container",
                                    children=[
                                        html.P(id="Total_Quantity_contratist", className="indicator_value"),
                                        html.P('Total Quantity', className="twelve columns indicator_text"),
                                ]),
                                html.Div(
                                    id="Total_Penalities_contratist_div",
                                    className="two columns indicator pretty_container",
                                    children=[
                                        html.P(id="Total_Penalities_contratist", className="indicator_value"),
                                        html.P('Total Penalities', className="twelve columns indicator_text"),
                                ]),
                            ],
                        )]
                    ),

########################### START parche histogramas ################################################################




            html.Div(
                className="twelve columns",
                children=[
                    html.Div(
                        className="padding-top-bot row",
                        children=[
                            html.Div(
                                className="six columns",
                                style={'margin-right': '15px', 'margin-left': '0px'},
                                children=[
                                    html.Div(children='''Total amount.'''),
                                    dcc.Graph(
                                        id='amount_graph_contratist',
                                        figure={
                                            'data': [],
                                            'layout': {
                                                #'title': 'Dash Data Visualization'
                                            }
                                        }

                                    ),
                                ]
                            ),
                            html.Div(
                                className="six columns",
                                style={'margin-right': '0px', 'margin-left': '15px'},
                                children=[
                                    html.Div(children='''Total Additions.'''),
                                    dcc.Graph(
                                        id='quantity_graph_contratist',
                                        figure={
                                            'data': [],
                                            'layout': {
                                                #'title': 'Dash Data Visualization'
                                                #"yaxis": {"showticklabels": False},
                                            }
                                        }
                                    ),
                                ]
                            ),

############################################ aqui estaba hitograma 3 ###########################################


                            html.Div(
                                className='six columns',
                                style={'margin-right': '15px', 'margin-left': '0px'},
                                children=[
                                    html.Div(children='''Quantity.'''),
                                    dcc.Graph(
                                        id='fisnished_graph_contratist',
                                        figure={
                                            'data': [],
                                            'layout': {
                                                #'title': 'Dash Data Visualization'
                                            }
                                        }
                                    ),
                                ]
                            ),


                            html.Div(
                                className='six columns',
                                style={'margin-right': '0px', 'margin-left': '15px'},
                                children=[
                                    html.Div(children='''Finished.'''),
                                    dcc.Graph(
                                        id='penalities_graph_contratist',
                                        figure={
                                            'data': [],
                                            'layout': {
                                                #'title': 'Dash Data Visualization'
                                            }
                                        }
                                    ),
                                ]
                            ),


############################ aqui estaba histograma 4 ##########################################################
                        ],
                    )]
                ),
########################### END parche histogramas ################################################################



########################### ultimos graficos #####################################################################
        ]
        )
    ])


########### Auxiliary functions ##################################

def my_strtr_contratist(cadena, reemplazo):    
    """Reemplazo múltiple de cadenas en Python."""
    import re
    regex = re.compile("(%s)" % "|".join(map(re.escape, reemplazo.keys())))
    return regex.sub(lambda x: str(reemplazo[x.string[x.start() :x.end()]]), cadena)

########################################################################



#####################################################################################################
# CALLBACKS 
#####################################################################################################


@app.callback(                              ###### HISTOGRAMAS ENTIDAD #####

    [
        dash.dependencies.Output("amount_graph_contratist", "figure"),
        dash.dependencies.Output("quantity_graph_contratist", "figure"),
        dash.dependencies.Output("fisnished_graph_contratist", "figure"),
        dash.dependencies.Output("penalities_graph_contratist", "figure"),
        dash.dependencies.Output('Total_Amount_contratist', 'children'),
        dash.dependencies.Output('Total_Quantity_contratist', 'children'),
        dash.dependencies.Output('Total_Penalities_contratist', 'children'),
    ],
    (    
        dash.dependencies.Input('date-range_contratist', 'start_date'),
        dash.dependencies.Input('date-range_contratist', 'end_date'),
        dash.dependencies.Input('department_dropdown_contratist', 'value'),
        dash.dependencies.Input('level_dropdown_contratist', 'value')
    ),
)
def update_entity_plot_contratist(start_date, end_date, value_department, value_level):

    print("Inicia consulta....")

    sql3 = """
    SELECT *
	FROM contratos_contratista
    WHERE fecha_ini_ejec_contrato >= 'Start_date'
    AND fecha_ini_ejec_contrato <= 'End_date'
    """

    if value_department != 'All':
        sql3 += """
        AND departamento_entidad = '{}'
        """.format(value_department)

    if value_level != 'All':
        sql3 += """
        AND orden_entidad = '{}'
        """.format(value_level)

    reemplazo = { 'Start_date' : start_date.split('T')[0], 'End_date' : end_date.split('T')[0]}
    print(my_strtr_contratist(sql3, reemplazo))
    
    df_ds4a = pd.read_sql(my_strtr_contratist(sql3, reemplazo), con=engine, parse_dates=('Entry time',))

    print("Fin consulta.....")

    #df_ds4a = pd.read_sql(sql3, con=engine)

    df_ds4a["terminado"]=[int(x) for x in df_ds4a["terminado"]]
    df_ds4a["sancion"]=[int(x) for x in df_ds4a["sancion"]]    
    colInteres = ['nom_raz_social_contratista', 'fecha_ini_ejec_contrato', 'cuantia_contrato','number_contracts', 'sancion', 'terminado', 'nivel_entidad']
    df_ds4a_extras = {"cuantia_contrato":["sum","max","count"],"sancion":"sum","terminado":"sum","nivel_entidad":"sum"}
    cleaned_df = df_ds4a[colInteres].groupby("nom_raz_social_contratista").agg(df_ds4a_extras).reset_index()
    cleaned_df.columns = ["_".join(x) for x in cleaned_df.columns.ravel()]
    cleaned_df['cuantia_contrato_sum'] = cleaned_df['cuantia_contrato_sum']/1000000000

    df_contratist = cleaned_df.sort_values(by=("cuantia_contrato_sum"),ascending=False)[:15].sort_values(by=("cuantia_contrato_sum"), ascending=True)
    data1 = [
        {
            "x": df_contratist['cuantia_contrato_sum'],
            "y": df_contratist['nom_raz_social_contratista_'],
            "text": df_contratist['nom_raz_social_contratista_'],
            "textposition": "auto",
            "type": "bar",
            "orientation" : 'h',
            "name": "",
        }
    ]

    df_contratist = cleaned_df.sort_values(by=("nivel_entidad_sum"),ascending=False)[:15].sort_values(by=("nivel_entidad_sum"), ascending=True)
    data2 = [
        {
            "x": df_contratist['nivel_entidad_sum'],
            "y": df_contratist['nom_raz_social_contratista_'],
            "text": df_contratist['nom_raz_social_contratista_'],
            "textposition": "auto",
            "type": "bar",
            "orientation" : 'h',
            "name": "",
        }
    ]

    df_contratist = cleaned_df.sort_values(by=("cuantia_contrato_count"),ascending=False)[:15].sort_values(by=("cuantia_contrato_count"), ascending=True)
    data3 = [
        {
            "x": df_contratist['cuantia_contrato_count'],
            "y": df_contratist['nom_raz_social_contratista_'],
            "text": df_contratist['nom_raz_social_contratista_'],
            "textposition": "auto",
            "type": "bar",
            "orientation" : 'h',
            "name": "",
        }
    ]

    df_contratist = cleaned_df.sort_values(by=("terminado_sum"),ascending=False)[:15].sort_values(by=("terminado_sum"), ascending=True)
    data4 = [
        {
            "x": df_contratist['terminado_sum'],
            "y": df_contratist['nom_raz_social_contratista_'],
            "text": df_contratist['nom_raz_social_contratista_'],
            "textposition": "auto",
            "type": "bar",
            "orientation" : 'h',
            "name": "",
        }
    ]

    layout = {
        #"height": "550",
        "autosize": True,
        "margin": dict(t=30, b=30, l=20, r=20, pad=4),
        "yaxis": {"showticklabels": False},
    }

    tmp_suma_cuantia = cleaned_df['cuantia_contrato_sum'].sum()
    tmp_suma_cantidad = int(cleaned_df['cuantia_contrato_count'].sum())
    tmp_suma_sancianes = int(cleaned_df['sancion_sum'].sum())

    return {"data": data1, "layout": layout}, {"data": data2, "layout": layout}, {"data": data3, "layout": layout}, {"data": data4, "layout": layout}, f'{tmp_suma_cuantia:0.2f} KM', f'{tmp_suma_cantidad:d}', f'{tmp_suma_sancianes:d}'


################################################################################
# Callback to update the posible values of department
################################################################################
@app.callback(
    dash.dependencies.Output('department_dropdown_contratist', 'value'),
    [
        dash.dependencies.Input('department_dropdown_contratist', 'options')
    ]
)
def update_RegionDropdown_value_contratist(department_select):
    """updates the region dropdown value"""
    return department_select[0]['value'] 

################################################################################
# Callback to update the posible values of level
################################################################################
@app.callback(
    dash.dependencies.Output('level_dropdown_contratist', 'value'),
    [
        dash.dependencies.Input('level_dropdown_contratist', 'options')
    ]
)
def update_LevelDropdown_value_contratist(level_select):
    """updates the region dropdown value"""
    return level_select[0]['value'] 