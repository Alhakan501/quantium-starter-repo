
from dash import html,dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import app_code.components_ids as id
import dash_bootstrap_components  as dbc


def main_component() -> html.Div:
    return html.Div(
        id=id.header_label,
            children=[
                    html.Div(
                    id=id.title,
                        children=[
                            html.H4("SOUL FOODS",id='header'),
                            html.H6("Pink Morsel Sales",id='sub-header',)
                            ]),
                    radio_items(items),
                ])
    












def line_graph(dataframe:pd.DataFrame,cut_off_date,last_recorded_date,region)->px.line:
    fig=px.line(dataframe, y='sales', x='date',labels={"date": "Date", "sales": "Total Sales ($)"},title=f"Total Sales by Date for {region} region")
    fig.add_vline(x=cut_off_date,exclude_empty_subplots=True,line_width=1, line_dash="dash", line_color="yellow")
    fig.add_hline(y='$1565',line_width=1, line_dash="dash",line_color='gray') 
    fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)', 
    title_font_size=20,
    title_font_color="white",  
    xaxis=dict(showgrid=True,gridcolor='rgba(200,200,200,0.1)', tickfont=dict(color='rgba(255,255,255,0.4)', size=12),title=dict(font=dict(color='white', size=20))),    
    yaxis=dict(showgrid=True,gridcolor='rgba(200,200,200,0.1)', tickfont=dict(color='rgba(255,255,255,0.4)', size=11),title=dict(font=dict(color='white', size=20))),    
    )
    fig.add_vrect(x0=cut_off_date,x1=last_recorded_date,line_width=0, fillcolor="skyblue", opacity=0.1)
    fig.add_annotation(x=cut_off_date,  y=160, text="JANUARY 15 2021", showarrow=True,  arrowhead=7,  ax=-100,   ay=-35  )
    return fig
















def bar_chart(data_frame,region)->dcc.Graph:
    fig = px.bar(data_frame,x='Period',y='Total Sales',title=f'Overall Total Sales for {region} region',range_y=[0,8000000] )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  
        plot_bgcolor='rgba(0,0,0,0)', 
        xaxis=dict(showgrid=False, gridcolor='rgba(200,200,200,0.1)',tickfont=dict(color='rgba(255,255,255,0.4)', size=11),title=dict(font=dict(color='white', size=16))),  
        yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.1)',tickfont=dict(color='rgba(255,255,255,0.4)', size=11),title=dict(font=dict(color='white', size=16)) ),
        title_font_size=20,
        title_font_color="white",
        legend_title_font_color="green")
    fig.update_traces(
        texttemplate='%{y}', 
        textposition='outside',
        textfont=dict(size=12, color='white') ,
        marker=dict(color=['rgb(7, 77, 181)', 'rgb(14, 96, 202)', 'orange']) )
    return fig





def pie_chart(data_frame,region)->dcc.Graph:
    fig = px.pie( data_frame,names='Period',values='Total Sales',title=f'Overall Total Sales for {region} region',hole=0.5,)
    fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)',  
    title_font_size=20,
    title_font_color="white",
    legend=dict(
        x=1, 
        y=1.3,
        bgcolor='rgba(200,200,200,0.1)',
        bordercolor='steelblue', 
        borderwidth=2, 
        font=dict(
            family='Arial', 
            size=14, 
            color='white' ),),)
    return fig













def radio_items(items:list)->dcc.RadioItems:
    return  html.Div(
       id=id.radio_div,
        children=[ 
            dcc.RadioItems(
            items,
            items[0],
            id=id.radio_items,
            inline=True
    )] )









items=['all','east','west','north','south']
app_frame=[dbc.Container(id=id.body,
            children=[
                main_component(), 
               
                

               html.Div(className='row_0',
                         children=[
                           html.Div(className='line_card',
                         children=[
                            dcc.Graph(id=id.line_graph)])
                         ]),
                
                html.Div(className='row_1',
                         children=[
                           
                                html.Div(className='card',
                                    children=[
                                    dcc.Graph(id=id.bar_graph)]),

                                html.Div(className='card',
                                    children=[
                                    dcc.Graph(id=id.pie_graph)])
                            
                         ])
                         ])]


