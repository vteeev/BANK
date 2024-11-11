import random
import datetime
import csv
import os
class User:

    user_id_counter = 100000

    def __init__(self, name, surname, e_mail, passward):
        self.name=name
        self.surname=surname
        self.e_mail=e_mail
        self.password=passward

        self.pin="0000"
        self.balance=0.0
        self.user_id=self.__generate_unique_id()

        self.transactionMenager=TransactionManager(self.user_id)

    def __generate_unique_id(self):

        User.user_id_counter += 1
        return User.user_id_counter
    
    
    def show(self):
        print(f"Name: {self.name}   Nazwisko: {self.surname}")
        print(f"Balance: {self.balance}")
        print(f"Id: {self.user_id}")

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

    payment_id_counter = 1234567

    def __init__(self, amount):
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.payment_id = self.generate_unique_payment_id()

    @classmethod
    def generate_unique_payment_id(cls):           
        cls.payment_id_counter += 1
        return cls.payment_id_counter

class Deposit(Payment):

    sign='+'
    def __init__(self, amount, typ):

        super().__init__(amount)
        self.typ=typ
        print(f"{self.payment_id}  {self.timestamp}")

    def to_dict(self):
        return {"payment_id": self.payment_id, "kwota": self.amount, "typ": self.typ}


class Withdrawal(Payment):

    sign='-'
    def __init__(self, amount, typ):

        super().__init__(amount)
        self.typ=typ
        print(f"{self.payment_id}  {self.timestamp}")
    
    def to_dict(self):
        return {"payment_id": self.payment_id, "kwota": self.amount, "typ": self.typ}

class Transfer(Payment):

    sign='-'
    def __init__(self, amount, typ, recipient):

        super().__init__(amount)
        self.typ=typ
        self.recipient = recipient
        print(f"{self.payment_id}  {self.timestamp}")

    def to_dict(self):
        return {"payment_id": self.payment_id, "kwota": self.amount, "typ": self.typ, "Nr konta": self.recipient}

class TransactionManager:
    def __init__(self, user_id):
        self.user_id = user_id

        self.transaction_history = TransactionHistory(user_id)

    def make_deposit(self, amount, typ):
        deposit = Deposit(amount, typ)

        self.transaction_history.add_transaction(deposit)

    def make_withdrawal(self, amount, typ):
        withdrawal = Withdrawal(amount,typ)

        self.transaction_history.add_transaction(withdrawal)

    def make_transfer(self, amount, typ, recipient_id):
        transfer = Transfer(amount, typ, recipient_id)

        self.transaction_history.add_transaction(transfer)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

class TransactionHistory:
    def __init__(self, user_id):
        self.user_id = user_id
        self.transactions = []

        self.load_transactions()

    def add_transaction(self, transaction):
        if hasattr(transaction, "to_dict"):
            transaction = transaction.to_dict()
        self.transactions.append(transaction)
        print(f"Transakcja dodana dla użytkownika: {self.user_id}")
        self.save_transactions()

    def save_transactions(self):


        """Zapisuje bieżącą listę transakcji do pliku CSV."""
        with open(f"baza_danych/historia_{self.user_id}.csv", "w", newline='', encoding="utf-8") as plik:
            writer = csv.DictWriter(plik, fieldnames=["payment_id", "kwota", "typ", "Nr konta"])
            writer.writeheader()
            writer.writerows(self.transactions)

    def load_transactions(self):
        """Wczytuje istniejącą listę transakcji z pliku CSV, jeśli istnieje."""
        try:
            with open(f"baza_danych/historia_{self.user_id}.csv", "r", encoding="utf-8") as plik:
                reader = csv.DictReader(plik)
                return [row for row in reader]
        except FileNotFoundError:
            return []
        
    def sum_kwota(self):
        """Sumuje wszystkie kwoty wczytanych transakcji."""
        total = 0
        all_transactions = self.load_transactions()

        for transaction in all_transactions:
            # Konwersja kwoty na liczbę (zwykle kwoty w CSV są zapisane jako ciąg znaków)
            try:
                total += float(transaction["kwota"])
            except ValueError:
                print(f"Nieprawidłowa kwota w transakcji: {transaction['kwota']}")
        
        return total
    
    def show_history(self):
        all_history=self.load_transactions()

        for x in all_history:
            print(f"payment_id: {x['payment_id']}    kwota: {x['kwota']}")
