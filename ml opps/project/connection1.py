import pymysql
import pandas as pd
from sqlalchemy import create_engine


class Connection:
    
    def __init__(self, host, port, username, password,database):
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        self.database=database
        self.conn=None
        self.cursor=None
    
    
    def connect_to_database(self):
        self.conn=pymysql.connect(host=self.host,port=self.port
                    ,user=self.username,password=self.password, 
                    database=self.database)
        self.cursor=self.conn.cursor()

    def create_database(self,db_name):
        self.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name} ')
        self.cursor.execute(f'USE {db_name}')
        
    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
     
    # Inserts a dataframe as a table in the database    
    def insert_df(self,df,table_name):
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user=self.username,
                               pw=self.password,
                               db='housing_data'))
        df.to_sql(table_name,con= engine,
                  if_exists='append',index=False)
    
    #Reading in the table to a dataframe    
    def read_sql(self,query):
        df=pd.read_sql(query,con=self.conn)
        
        return df
    
    #adding model to the model table
    def add_model(self,val,query):   
        val=(val)
        self.cursor.execute(query,val)
        self.conn.commit()
