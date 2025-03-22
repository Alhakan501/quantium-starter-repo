
from dash import Dash,html,callback,dcc
from  components import main_component , line_graph,bar_chart,pie_chart,radio_items,app_frame,dbc,id
from data_filtering import Data
from dash.dependencies import Input,Output












@callback(Output(component_id=id.line_graph,component_property='figure'), Input(component_id=id.radio_items,component_property='value') )
def sort_line_chart(val):
    data_class=Data()
    line_data=data_class.line_chart_data(val)
    val=val.capitalize()
    if val!='All':
        val=val+'ern'
    return line_graph(line_data[0],line_data[1],line_data[2],val)
   


  
@callback(Output(component_id=id.bar_graph,component_property='figure'), Input(component_id=id.radio_items,component_property='value'))
def  sort_bar_chart(val):
    data_class=Data()
    bar_data=data_class.bar_chart_data(val)
    val=val.capitalize()
    if val!='All':
        val=val+'ern'
    
    return bar_chart(bar_data,val)





@callback(Output(component_id=id.pie_graph,component_property='figure'), Input(component_id=id.radio_items,component_property='value'))
def  sort_pie_chart(val):
    data_class=Data()
    pie_data=data_class.bar_chart_data(val)
    val=val.capitalize()
    if val!='All':
        val=val+'ern'
    return pie_chart(pie_data,val)


