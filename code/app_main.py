
import dash_bootstrap_components as dbc

from callbacks import *



app=Dash()
app.layout=app_frame



if __name__=='__main__':
    app.run(debug=True)
