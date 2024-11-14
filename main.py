from classes import*
from users import*


def main(user):
    is_running=True

    operation=user.transactionMenager
    history=operation.transaction_history

    while is_running:
        print("**********************")
        print("   Banking Program")
        print("**********************")
        print("1. Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Make transfer")
        print("5.Show History")
        print("6.Exit")
        print("**********************")
        choise=input("Enter choice (1/4): ")

        match choise:
            case '1':
                print(f"Balance: {history.sum_kwota()}")
            case '2':

                value=float(input("Suma wplaty: "))
                operation.make_deposit(value,"deposit")

            case '3':

                value=float(input("Suma wyplaty: "))*(-1)
                operation.make_withdrawal(value,"withdrawal")
 
            case '4':
                value=float(input("Kwota przelewu: "))
                recipiate=int(input("Nr konta: "))*(-1)
                operation.make_transfer(value,"bank-transfer",recipiate)
            case '5':
                history.show_history()
            case '6':
                is_running=False
            case _:
                print("Bledne dane wprowadz jeszcze raz!")
    
def start_login():
    print("--------------------")
    user_id = int(input("Login ID: "))
    password = input("Password: ")
    print("--------------------")

    # Check if the user exists in the Users list
    user = next((u for u in Users if u.user_id == user_id and u.password == password), None)
    
    if user:
        print(f"Hello {user.name} :)")
        main(user)
    else:
        print("Invalid login credentials :(")

start_login()