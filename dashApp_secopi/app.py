import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output


#app = dash.Dash()
#SERVER = flask.Flask(__name__)
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=SERVER)


app = dash.Dash(__name__)
server = app.server
#correcciones
#app.config.supress_callback_exceptions = True
#In case you missed it in the Dash change log, this misspelled fallback was removed in 1.0.0.

app.config.suppress_callback_exceptions = True





