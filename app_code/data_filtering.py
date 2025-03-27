import pandas as pd


class Data:
    def __init__(self):
        self.df=pd.read_csv('./data/final.csv')
        



    def line_chart_data(self,query:str=None)->list:
        
        if query=='all' or not query:
            df=self.df.copy()
        else:
            df=self.df[self.df['region'] == query].copy()
        
        cut_off=pd.to_datetime('2021-01-15')
        
        df['date']=pd.to_datetime(df['date'])
        
        final_date=df['date'].astype(str).to_list()[-1]
      
        
        return [df,cut_off,final_date]








    def bar_chart_data(self,query:str=None):

        if query=='all' or not query:
            df=self.df.copy()
        else:
            df=self.df[self.df['region'] == query].copy()

        before= df.loc[self.df['date'] < '2021-01-15']
        total_sales_before=before['sales'].apply(lambda x : float(str(x).replace("$",''))).sum()
       
        
        after= df.loc[self.df['date'] >= '2021-01-15']
        
        total_sales_after=after['sales'].apply(lambda x : float(str(x).replace("$",''))).sum()
        
        new_dict = {'Period': ['Before January 15 2021', 'After January 15 2021'],
                        'Total Sales': [total_sales_before, total_sales_after]
                    }
        
        df=pd.DataFrame(new_dict)
        
        return  df







    def radio_data(self):
        region=self.df['region'].unique().tolist()       
        region.append('all')
        return sorted(region)




# Data().line_chart_data()