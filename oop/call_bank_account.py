from bank_account import BankAccount

def main():
    my_account=BankAccount(25869,'leah_itzinger', 500)
    print(my_account)
    my_account.deposit(150)
    my_account.withdraw(50)

main()