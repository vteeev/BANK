from classes import*
from users import*


def main(x):
    is_running=True
    while is_running:
        print("**********************")
        print("   Banking Program")
        print("**********************")
        print("1. Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Make transfer")
        print("5.Exit")
        print("**********************")
        choise=input("Enter choice (1/4): ")

        match choise:
            case '1':
                print(f"Balance: {x.get_balance()}")
            case '2':
                value=float(input("Suma wplaty: "))
                x.make_deposit(value)
            case '3':
                value=float(input("Suma wyplaty: "))
                x.make_withdrawal(value)
            case '4':
                value=float(input("Kwota przelewu: "))
                recipiate=str(input("Nr konta: "))
                x.make_transfer(value,recipiate)
            case '5':
                is_running=False
            case _:
                print("Bledne dane wprowadz jeszcze raz!")
    
def star_login():
    print("--------------------")
    user_id=int(input("Login: "))
    password=str(input("Passward: "))
    print("--------------------")

    is_you=False
    for x in Users:
        if user_id==x.user_id and password==x.password:
            print(f"Hello {x.name} :)")
            main(x)
            is_you=True
        else:
            pass

    if is_you:
        print()
    else:
        print("Invalid data :(")

star_login()