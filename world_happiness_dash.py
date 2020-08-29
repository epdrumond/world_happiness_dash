# 1. Import libraries ---------------------------------------------------------
import pandas as pd
import plotly.graph_objs as go

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

# 2. Load data ----------------------------------------------------------------
data = pd.read_csv('world_happiness_2015_to_2019.csv', sep = ';')

# 3. Create application -------------------------------------------------------
app = dash.Dash()

#Define colors dict
colors = {
    'background': '#dee3e7',
    'plot_background': '#fafcfe',
    'text': '#3e4041'
    }

#Create layout
app.layout = html.Div([
    html.Div(html.H1(children = 'World Happiness Ranking - 2015 to 2019'),
             style = {'fontSize': 15,
                      'font-family': 'helvetica', 
                      'textAlign': 'center'
                      }),
    html.Div([
        html.Div([html.H2(data['Country'].nunique(), style = {'margin-bottom': '-5px'}),
                  html.H3('Countries', style = {'fontSize': 11, 'color': '#7f8187'})],
                 style = {'textAlign': 'center', 
                          'font-family': 'arial',
                          'width': '10%',
                          'display': 'inline-block',
                          'border': '2px white outset',
                          'borderRadius': '10px',
                          'backgroundColor': colors['plot_background'],
                          'margin-right': '5px'}),
        html.Div([html.H2(data['Region'].nunique(), style = {'margin-bottom': '-5px'}),
                  html.H3('Regions', style = {'fontSize': 11, 'color': '#7f8187'})
                  ],
                 style = {'textAlign': 'center', 
                          'font-family': 'helvetica',
                          'width': '10%',
                          'display': 'inline-block',
                          'border': '2px white outset',
                          'borderRadius': '10px',
                          'backgroundColor': colors['plot_background']})
        ],
        style = {'backgroundColor': colors['background']}
        )
    ],
    style = {'font-family': 'helvetica',
             'backgroundColor': colors['background']})

# 4. Run application ----------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug = True)