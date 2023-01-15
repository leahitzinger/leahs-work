class BankAccount:
    def __init__(self,account_number, name, balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,deposit):
        self.balance+=deposit
        print('your balance is now' ,self.balance)

    def withdraw(self,withdraw):
        self.balance-=withdraw
        print('your balance is now' ,self.balance)

    def __str__(self):
       return 'Hi {} account number {} your balance is {}'.format(self.name,self.account_number,self.balance)
