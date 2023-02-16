goods = ['Milk Chocolate', 'White Chocolate', 'Dark Chocolate',
         'Semisweeet Chocolate', 'Swiss Chocolate', 'Perlino Chocolate']
price_goods = {'Milk Chocolate': 25, 'White Chocolate': 30, 'Dark Chocolate': 20,
               'Semisweeet Chocolate': 22, 'Swiss Chocolate': 45, 'Perlino Chocolate': 35}

print('Welcome to Chocolate Fantasies!\nChocolate is always the answer...\nWe sell the following varieties:')
for each in goods:
    print(each)
buy_more='yes'
item_list=[]
while buy_more=='yes':  
    item = input('What would you like to purchase today')
    try:
        amount = int(input('How many can we offer you'))
    except ValueError:
        amount = int(input('pls. re-enter a valid amount'))
    try:
        price=price_goods[item] *amount
        confirm=input('Please confirm your purchase of {} {} for {}NIS. yes or no'.format(amount,item,price))
        if confirm=='yes':
            item_list.append([item,amount,price,price_goods[item]])
        buy_more=input('Would you like to buy anything else today? yes or no')
    except KeyError:
        print('your input was not recognized')
        buy_more='yes'
    except:
        print('your input was invalid')
        buy_more='yes'

print('receipt:')
total=0
for x in item_list:
    print(x[0] ,x[3] ,'nis x ' , x[1] , ' =', x[2] ,'nis')
    total+=x[2]
 
print('your total bill is {}'.format(total))

    





























    
