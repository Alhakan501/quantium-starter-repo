from dash import Dash,dcc,html

from dash.dependencies import Input,Output
import dash_bootstrap_components  as dbc

from  components import *
from data_filtering import read_dataset


data=read_dataset()



app=Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=[main_component(), 
         
            line_graph(data[0],data[1],data[2])]






if __name__=='__main__':
    app.run(debug=True)
