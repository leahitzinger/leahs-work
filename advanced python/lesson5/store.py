import logging
import os
import pandas as pd
import re

CURR_DIR = os.path.dirname(__file__)
LOG_FOLDER = CURR_DIR + '/store_logs'

logging.basicConfig(filename= LOG_FOLDER +'/my_store_logs.txt',
filemode='a+',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%Y-%m-%d %H:%M:%S',
#datefmt='%H:%M:%S',
level=logging.INFO)


price_goods = {'Milk Chocolate': 25, 'White Chocolate': 30, 'Dark Chocolate': 20,
               'Semisweet Chocolate': 22, 'Swiss Chocolate': 45, 'Perlino Chocolate': 35}

print('Welcome to Chocolate Fantasies!\nChocolate is always the answer...\nWe sell the following varieties:')
for each in price_goods:
    print(each)
buy_more='yes'
item_list=[]
while buy_more=='yes':  
    item = input('What would you like to purchase today')
    try:
        amount = int(input('How many can we offer you?'))
    except ValueError:
        amount = int(input('pls. re-enter a valid amount'))
    try:
        price=price_goods[item] *amount
        confirm=input('Please confirm your purchase of {} {} for {}NIS. yes or no'.format(amount,item,price))
        if confirm=='yes':
            item_list.append([item,amount,price,price_goods[item]])
            logging.info('The customer added {} to cart.'.format(item))
        buy_more=input('Would you like to buy anything else today? yes or no')
    except KeyError:
        print('your input was not recognized')
    except:
        print('your input was invalid')

name=input('Please enter your name')
phone=input('Please enter your phone number')
bool1=False
while bool1==False:    
    credit_card=input('Please enter credit card number')
    bool1=bool(re.search('\d{16}', credit_card))
    
logging.info('credit card went through')
    
print('receipt:')
total=0
df=pd.DataFrame(columns=['item','amount','total','price','name','phone number','order id'])
df1=pd.read_csv('C:/Users/admin/Documents/guided project/advanced python/lesson5/store_csv.csv')
try:
    id=df1['order id'][len(df1)-1]+1
except:
    id=10000000
for x in item_list:
    # print(x[0] ,x[3] ,'nis x ' , x[1] , ' =', x[2] ,'nis')
    total+=x[2]
    x.append(name)
    x.append(phone)
    x.append(id)
    df.loc[len(df)]=x
print(df)

df3=pd.concat([df1,df])
df3.to_csv(path_or_buf='C:/Users/admin/Documents/guided project/advanced python/lesson5/store_csv.csv',index=False)
logging.info('Order went through with a total of {} ils '.format(total))
 
print('your total bill is {}.'.format(total))


    





























    
