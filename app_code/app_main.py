
from dash import  Dash


from app_code.callbacks import *



app=Dash()
app.layout=app_frame



if __name__=='__main__':
    app.run(debug=True)
