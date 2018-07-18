from abc import abstractmethod, ABCMeta
from random import randint


class Account(metaclass=ABCMeta):

    @abstractmethod
    def create_account(self, name, initial_deposit):
        return 0

    @abstractmethod
    def authenticate(self, name, account_no):
        return 0

    @abstractmethod
    def withdraw(self, withdrawal_amount):
        return 0

    @abstractmethod
    def deposit(self, deposit_amount):
        return 0

    @abstractmethod
    def display_balance(self):
        return 0


class SavingsAccount(Account):

    def __init__(self):
        # key => account_no; [key][0] => name; [key][1] => balance
        self.saving_accounts_list = {}

    def create_account(self, name, initial_deposit):
        self.account_no = randint(10000, 99999)
        self.saving_accounts_list[self.account_no] = [name, initial_deposit]
        print('Account creation was successful. You new account number is: ', self.account_no)

    def authenticate(self, name, account_no):
        if account_no in self.saving_accounts_list.keys():
            if self.saving_accounts_list[account_no][0] == name:
                print('Authentication Successful!')
                self.account_no = account_no
                return True
            else:
                print('Authentication Failed!!!')
                return False
        else:
            print('Authentication Failed!!!')
            return False

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.saving_accounts_list[self.account_no][1]:
            print('Insufficient balance!')
        else:
            self.saving_accounts_list[self.account_no][1] -= withdrawal_amount
            print('Withdrawal was successful.')
            self.display_balance()

    def deposit(self, deposit_amount):
        self.saving_accounts_list[self.account_no][1] += deposit_amount
        print('Deposit was successful.')
        self.display_balance()

    def display_balance(self):
        print('Available balance: ', self.saving_accounts_list[self.account_no][1])


saving_account = SavingsAccount()

while True:
    print('Enter 1 to create a new account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to exit')

    user_choice = int(input())
    if user_choice is 1: # create a new account
        print('Enter your name: ')
        name = input()
        print('Enter your initial deposit: ')
        initial_deposit = int(input())
        saving_account.create_account(name, initial_deposit)
    elif user_choice is 2: # access the account
        print('Enter your name: ')
        name = input()
        print('Enter your account no: ')
        account_no = int(input())

        auth_status = saving_account.authenticate(name, account_no)
        if auth_status:
            while True:
                print('Enter 1 to Withdraw')
                print('Enter 2 to Deposit')
                print('Enter 3 to see your balance')
                print('Enter 4 to go back to the previous menu')

                user_choice = int(input())

                if user_choice is 1: # Withdraw
                    print('Enter your withdrawal amount: ')
                    withdrawal_amount = int(input())
                    saving_account.withdraw(withdrawal_amount)
                elif user_choice is 2: # Deposit
                    print('Enter your deposit amount: ')
                    deposit_amount = int(input())
                    saving_account.deposit(deposit_amount)
                elif user_choice is 3: # View Balance
                    saving_account.display_balance()
                elif user_choice is 4: # Return back
                    break

    elif user_choice is 3: # Exit
        quit()

