import multiprocessing
class Vault:
    def __init__(self,name,account ,sum):
        self.sum=sum
        self.name=name
        self.account=account
    
    def create_account(self,account):
        self.sum=0
        self.account=account

    def update_accounts(self,deposit,shared_value):
        self.sum+=deposit
        with shared_value.get_lock():
            shared_value.value += self.sum
vault1=Vault('leah itzinger', 'account1', 520)
vault2=Vault('leah itzinger', 'account2', 150)
vault3=Vault('leah itzinger', 'account3', 450)
vault4=Vault('leah itzinger', 'account4', 140)

shared_value = multiprocessing.Value('i')

process1 = multiprocessing.Process(target=vault1.update_accounts, args=[520, shared_value])
process2 = multiprocessing.Process(target=vault2.update_accounts, args=[60, shared_value])
process3 = multiprocessing.Process(target=vault3.update_accounts, args=[120, shared_value])
process4 = multiprocessing.Process(target=vault4.update_accounts, args=[450, shared_value])


if __name__ == '__main__':
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    print(shared_value.value) 



    

        
