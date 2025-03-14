
from dash import html,dcc
import pandas as pd
import plotly.express as px



def main_component() -> html.Div:
    return html.Div(
            children=[
                    html.H3("Pink Morsel Sales "),
                  
                
                ]
    )
    
    
def line_graph(dataframe:pd.DataFrame,x:pd.Series,y:pd.Series)->dcc.Graph:
    
    fig = px.line(dataframe, x=x, y=y, title=f"{y} Over {x}")
    
    return dcc.Graph(id='sales-line-graph', figure=fig)