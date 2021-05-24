class Bank_mem:
    def __init__(selt, name, balance_account):
        self.name = name
        self.balance_account = balance_account

    def __check(self, withdraw_money):
        if self.balance_account - self.withdraw_money >= 20000:
            return True
        return False
        # if self.balance_account <= 20000 :
        #     print('your account balance is low!!!')
        #     print('your account balance is low!!!')
        # else :
        #     self.balance_account -= self.withdraw_money
    
    def deposit(self, deposit_money):
        self.balance_account += self.deposit_money
        print(self.balance_account)


    def withdraw(self, withdraw_money):
        self.withdraw_money.check()

    def transfer(self, name_2, transfer_money):
        self.name_2 = name_2
        self.transfer_money.check()
        self.transfer_money.withdraw(500)
        self.transfer_money.deposit(self.name_2)
