import pandas as pd
import numpy as np


class CreditCardStatement:
    def read(self,path):
        df=pd.read_csv(path,header=None,names=['store','spent','date'])
        return df
    
    def __init__(self,name):
        self.total=0
        self.name=name


    def read_file(self,df):
        for index, row in df.iterrows():
            store=row['store']
            amount=row['spent']
            date=row['date']
            if amount>200:
                print('we need you to confirm this payment. the amount is' ,amount, '$ in' ,store )
            else:
                print('you spent' ,amount , '$ in', store , 'on' ,date)
    
    
    def calculate_total(self,df):
        
        for index, row in df.iterrows():
            self.total+=row['spent']
        print('You have spent a total of', self.total , '$')

    def total_per_month(self,df):
        df['date'] = df['date'].astype("string")
        date=df['date'].str.split('/',n=1,expand=True)
        df['date_year']=date[1]
        table = pd.pivot_table(df, values='spent', index='date_year', aggfunc=np.sum)
        for index, row in table.iterrows():
            print('you spent a total of' ,row['spent'] ,'$ on '  ,index)           
    
    
    def __str__(self):
        welcome='Hello '
        welcome+=self.name
        return welcome

    def print_status(self):
        df=self.read('credit_card_bill.txt')
        self.read_file(df)
        self.calculate_total(df)
        self.total_per_month(df)

def main():
    my_credit=CreditCardStatement('leah')
    print(my_credit)
    my_credit.print_status()




   