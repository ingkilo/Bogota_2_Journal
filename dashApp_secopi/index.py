# Load main libraries
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

#df = pd.read_csv('aggr.csv', parse_dates=['Entry time'])

# Load apps
from app import app
from Apps import Summary, Score, Entities, Contratist
application =  app.server


#app.css.append_css({
#    "external_url": "https://codepen.io/uditagarwal/pen/oNvwKNP.css"
#})


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
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("dash-logo-new.png"),
                            id="plotly-image",
                            style={
                                "height": "30px",
                                "width": "auto",
                                "margin-top": "30px",
                                "margin-left": "25px",
                            },
                        )],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div([
                            html.H1(children="Group 2 DS4A Dashboard", style={'textAlign': 'center'}),
                        ])
                    ],
                    className='study-browser-banner row',
                    id="title",
                ),
            ],
            id="header",
            className="row flex-display",
            #style={"margin-bottom": "25px"},
        ),
#    html.Div([
#        html.Br(),
#        html.Br(),
#        html.Br(),
#        html.Br()
#        ]),
    html.Div([
        dcc.Tabs(
            id="tabs-with-classes",
            value='tab-1',
            parent_className='custom-tabs',
            className='custom-tabs-container ',
            children=[
                dcc.Tab(
                    label='Summary',
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
                dcc.Tab(
                    label='Entities',
                    value='tab-3',
                    className='custom-tab',
                    selected_className='custom-tab--selected',
                    style=tab_style, selected_style=tab_selected_style,
                    ),
                dcc.Tab(
                    label='Contratist',
                    value='tab-4',
                    className='custom-tab',
                    selected_className='custom-tab--selected',
                    style=tab_style, selected_style=tab_selected_style,
                    ),
                ],
            style={ 'display': 'inline-block','padding-right':'10%','width': '80%'}, 
            ),
        ],
        className= 'sticky-top row', )
    ]),
    html.Div(id='tabs-content-classes')
])

@app.callback   (Output('tabs-content-classes', 'children'),
                [Input('tabs-with-classes', 'value')])
def display_page(frame):
    """Changes content on different pages"""
    if frame == 'tab-1':
        return Summary.layout
    elif frame == 'tab-2':
        return Score.layout
    elif frame == 'tab-3':
        return Entities.layout
    elif frame == 'tab-4':
        return Contratist.layout
    else:
        return '404'

#corregido

if __name__ == '__main__':

    app.run_server(debug=True)
