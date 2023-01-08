import pandas as pd


class CreditCardStatement:
    def read(self,path):
        df=pd.read_csv(path,header=None,names=['store','spent','date'])
        return df

    def read_file(self,df):
        for index, row in df.iterrows():
            store=row['store']
            amount=row['spent']
            date=row['date']
            if amount>200:
                print('we need you to confirm this payment. the amount is' ,amount, '$ in' ,store )
            else:
                print('you spent' ,amount , '$ in', store , 'on' ,date)
            


my_credit=CreditCardStatement()
df=my_credit.read('credit_card_bill.txt')
my_credit.read_file(df)

