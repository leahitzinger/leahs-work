import multiprocessing
class Mastercard:
    def __init__(self, sum):
        self.sum= sum
    def mastercard_transaction(self, amount):
        if amount <= self.sum:
            self.sum-=amount
            print(self.sum)
            print('Your account will be charged with'+ str(amount))
        else:
            print('You do not have enough money in your account, please withdraw an amount, which is less than your balance:', self.balance)
if __name__ == '__main__':
    mastercard=Mastercard(10000)
    transactions=[40, 70, 900, 23, 45, 67, 2345]
    tasks = [multiprocessing.Process(target=mastercard.mastercard_transaction, args=[transaction]) for transaction in transactions]
    for process in tasks:
        process.start()
    for process in tasks:
        process.join()