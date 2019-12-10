################################################################################################
#### Dash application of Team 2 - Bogotá - DS4A
################################################################################################

# Load main libraries
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

df = pd.read_csv('aggr.csv', parse_dates=['Entry time'])

# Load apps
from app import app
from Apps import Landing, Score
application =  app.server
app.css.append_css({
    "external_url": ['https://codepen.io/uditagarwal/pen/oNvwKNP.css', 'https://codepen.io/uditagarwal/pen/YzKbqyV.css'],
})


tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    #'line-height': 'tab_height',
    #'height': '100px'
}

app.layout = html.Div([html.Div([
    html.Div([html.Br(),
    html.Br(),
    html.Br(),
    html.Br()]),
    html.Div([
        dcc.Tabs(
        id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container ',
        children=[
            dcc.Tab(
                label='Landing',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style=tab_style, selected_style=tab_selected_style
            ),
            dcc.Tab(
                label='Score',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected',
                style=tab_style, selected_style=tab_selected_style,

            ),
            
        ], style={ 'display': 'inline-block','padding-right':'10%','width': '80%'}, ),

],className= 'sticky-top row', )]),
html.Br(),html.Div(id='tabs-content-classes')])

@app.callback(Output('tabs-content-classes', 'children'),
[Input('tabs-with-classes', 'value')])
def display_page(tab):
    """Changes content on different pages"""
    if tab == 'tab-1':
        return Landing.layout
    elif tab == 'tab-2':
        return Score.layout
    else:
        return '404'


if __name__ == '__main__':

    app.run_server(debug=True)
