import pandas as pd



def read_dataset()->list:
    df=pd.read_csv('./data/final.csv')
    
    x = df['date']
    y = df['sales']
    return [df , x , y]