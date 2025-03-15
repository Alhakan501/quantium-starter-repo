
from dash import html,dcc
import pandas as pd
import plotly.express as plt
import plotly.graph_objects as go



def main_component() -> html.Div:
    return html.Div(
            children=[
                    html.H3("Pink Morsel Sales "),
                ])
    



def line_graph(dataframe:pd.DataFrame,cut_off_date,last_recorded_date,)->dcc.Graph:
    
    fig=plt.line(dataframe, y='sales', x='date',labels={"date": "Date", "sales": "Total Sales ($)"})
    
    fig.add_vline(x=cut_off_date,exclude_empty_subplots=True,line_width=2, line_dash="dash", line_color="green")
    
    fig.add_hline(y='$1565',line_width=1, line_dash="dash",line_color='gray') 
    
    
    fig.add_vrect(x0=cut_off_date,x1=last_recorded_date,line_width=0, fillcolor="yellow", opacity=0.1)
    
    fig.add_annotation(x=cut_off_date,  y=160, text="JANUARY 15 2021", showarrow=True,  arrowhead=7,  ax=-100,   ay=-35  )
    
    return dcc.Graph(figure=fig)