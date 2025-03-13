from dash import Dash,html,dcc
from dash.dependencies import Input,Output
import dash_bootstrap_components  as dbc
import pandas as pd
import plotly as plt


app=Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=html.Div(
    children=[
        html.Header('Dash App')
        ]
)






if __name__=='__main__':
    app.run(debug=True)
