import pandas as pd  #import the pandas library









def  read_merge_data_frame(csv_list:list)->pd.DataFrame:
    
    # read each file in the csv_file_list and store all the datframes. concate the dataframes to create a single dataframe  
    combined_data=pd.concat([pd.read_csv(csv_file) for csv_file in csv_list]) 
    
    return combined_data












def clean_dataframe(df:pd.DataFrame)->pd.DataFrame:
    
    # filter and keep rows that have a product value of 'pink mordel' , ensuring df is a copy to avoid modifying a slice
    df = df[df['product'] == 'pink morsel'].copy()  

    # convert quantity to integer 
    quantity= df['quantity'].astype(int)  

    # convert price to float (remove "$")
    price = df['price'].str.replace("$", "").astype(float)

    # create sales column
    df['sales'] = price * quantity
    
    # add the $ symbol to the sales column
    df['sales']=df['sales'].apply(lambda x: '$'+str(int(x))) 
    
    df.drop(columns=['product','price','quantity'],inplace=True)
    
    df=df[['sales','date','region'] ]
    
    return df
    
    
    
    
    
    
    
  
  
    
def create_csv(df:pd.DataFrame):
    print("Creating the output file 'final.csv'........")
    
    df.to_csv('data/final.csv',index=False)
    
    print('Successfully create file:  data/final.csv ')
    
     
  
   
    

    









if __name__=='__main__':
    
    csv_file_list=['data/daily_sales_data_0.csv','data/daily_sales_data_1.csv','data/daily_sales_data_2.csv']   # create a list of the .csv datasets 
    
    merged_df=read_merge_data_frame(csv_file_list)
    
    filtered_df=clean_dataframe(merged_df)
    
    create_csv(filtered_df)