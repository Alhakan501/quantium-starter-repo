import pandas as pd



def read_dataset()->list:
    
    df=pd.read_csv('./data/final.csv')
    
    cut_off=pd.to_datetime('2021-01-15')
    
    df['date']=pd.to_datetime(df['date'])
    
    final_date=df['date'].astype(str).to_list()[-1]
    
    return [df,cut_off,final_date]



