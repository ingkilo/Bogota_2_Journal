################################################################################################
#### Dash application of Team 2 - Bogota - DS4A
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
import plotly.graph_objects as go
import json


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

mapbox_access_token = 'pk.eyJ1IjoibmV3dXNlcmZvcmV2ZXIiLCJhIjoiY2o2M3d1dTZiMGZobzMzbnp2Z2NiN3lmdyJ9.cQFKe3F3ovbfxTsM9E0ZSQ'

with open("us.json") as geofile:
    geojson_layer = json.load(geofile)


col_state_abbrev = {
'Amazonas':'AMA',
'Antioquia':'ANT',
'Arauca':'ARA',
'Atlántico':'ATL',
'Bogotá D.C.':'BOG',
'Bolívar':'BOL',
'Boyacá':'BOY',
'Caldas':'CAL',
'Caquetá':'CAQ',
'Casanare':'CAS',
'Cauca':'CAU',
'Cesar':'CES',
'Chocó':'CHO',
'Córdoba':'COR',
'Cundinamarca':'CUN',
'Guainía':'GUA',
'Guaviare':'GUV',
'Huila':'HUI',
'La Guajira':'GUA',
'Magdalena':'MAG',
'Meta':'MET',
'Nariño':'NAR',
'Norte De Santander':'NSA',
'Putumayo':'PUT',
'Quindío':'QUI',
'Risaralda':'RIS',
'San Andrés y Providencia':'SAP',
'Santander':'SAN',
'Sucre':'SUC',
'Tolima':'TOL',
'Valle del Cauca':'VDC',
'Vaupés':'VAU',
'Vichada':'VIC',
}


sql3 = """
SELECT departamento_entidad, cuantia_contrato
FROM fix_secopi
LIMIT 500;
"""
df = pd.read_sql(sql3, con=engine)

df['State_abbr'] = df['departamento_entidad'].map(col_state_abbrev)
df['cuantia_contrato'] = df['cuantia_contrato']/3500                    #Contracts on dollars
states_grouped = df.groupby(['State_abbr'], as_index=False).sum()
states_grouped['Sales_State'] = states_grouped[['State_abbr', 'cuantia_contrato']].apply(lambda x: 'Contracts for {}: {:.2f}$'.format(x[0], x[1]), axis=1)
states_grouped.head()




app.layout = dcc.Graph(
    id="mapbox",
    figure={
        'data': [
            dict(
                type='choropleth',
                autocolorscale=True,
                locations=states_grouped['State_abbr'],
                z=states_grouped['cuantia_contrato'],
           )
                ],
        "layout": dict(
            autosize=True,
            hovermode="closest",
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=(41.895566, 12.448533),
                #center=(4.6097102, -74.081749),
                style="dark",
                pitch=0,
                zoom=6,
                layers=[
                    dict(
                        type="fill",
                        sourcetype="geojson",
                        source=geojson_layer,
                        color='YlGn',
                        opacity=0.8,
                        below="state-label-sm"
                    )
                ]
            )
        )
    },
    style={"height": "100vh"}
)

if __name__ == '__main__':
    app.run_server(debug=False)