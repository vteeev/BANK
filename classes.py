import random
import datetime


class User:

    payment_=1234567
    counter = 100000

    def __init__(self, name, surname, e_mail, passward):
        self.name=name
        self.surname=surname
        self.e_mail=e_mail
        self.password=passward

        self.pin="0000"
        self.balance:.2=0
        self.user_id = self.__generate_unique_id()

        self.transactions = []
        self.transactionHistory=TransactionHistory(User.user_id)

    def __generate_unique_id(self):

        User.counter += 1
        return User.counter
    
    def generate_unique_payment_id():
            
            User.payment_ += 1
            return User.payment_
    
    def show(self):
        print(f"Name: {self.name}   Nazwisko: {self.surname}")
        print(f"Balance: {self.balance}")
        print(f"Id: {self.user_id}")

    def make_deposit(self,  amount):
        deposit = Deposit( amount)
        self.transactions.append(deposit)

    def make_withdrawal(self, amount):
        withdrawal = Withdrawal( amount)
        self.transactions.append(withdrawal)

    def make_transfer(self, amount, recipient):
        transfer = Transfer(amount, recipient)
        self.transactions.append(transfer)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.sign=='+':
                balance += transaction.amount
            else:
                balance -= transaction.amount
        return balance


class Admin(User):
    def __init__(self, name, surname, e_mail, passward):
        Admin.name=name
        Admin.surname=surname
        Admin.e_mail=e_mail
        Admin.password=passward
    
    def change_balance():
        pass

###

class Payment:

    def __init__(self, amount):
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def recipt(self):
        print()
        print(f"PARAGON     Data: {Payment.timestamp}")
        print(f"Kwota depozytu: {self.amount}")
        print()


class Deposit(Payment):
    sign='+'
    def __init__(self,  amount):
        super().__init__(amount)
   

class Withdrawal(Payment):
    sign='-'
    def __init__(self,  amount):
        super().__init__(amount)


class Transfer(Payment):
    sign='-'
    def __init__(self,  amount, recipient):
        super().__init__(amount)
        self.recipient = recipient

####

class TransactionHistory:
    def init(self, user_id):
        self.user_id = user_id
        self.transactions = []


