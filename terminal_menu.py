from customer_class import Customer
from datetime import datetime

def main_menu():
    """creates an infinite loop that presents the user with a list of options for interacting with an account?"""
    stop = False
    while stop is False:
        print("would you like to add a new customer (1), delete a customer (2), edit a customers details(3),"
              " make a deposit(4), make a withdrawal(5) or search for a client(6), or logout (7)")
        choice = str(input())
        if choice == "1":
            create_new_account()
        elif choice == "2":
            print("hi")
        elif choice == "3":
            print("hi")
        elif choice == "4":
            print("hi")
        elif choice == "5":
            print("hi")
        elif choice == "6":
            print("hi")
        elif choice == "7":
            stop = True
        else:
            print("unexpected input, please try again")


def create_new_account():
    """gives the user a way to create a new line in the csv file which represents a user"""
    first_name = input("What is the first name of your user?")
    last_name = input("What is the last name of your user? ")
    user_title = input("What is your user's title? ")
    preferred_pronouns = input("What are your user's preferred pronouns? ")
    print("What date was your user born? ")
    date_entry = input('Enter a date (i.e. dd/mm/yyyy) ')
    try:
        day, month, year = map(int, date_entry.split('/'))
        date = datetime(day, month, year)
    except ValueError:
        print("Incorrect format")
    user_occupation = input("What is your user's occupation? ")
    user_balance = input("What is your user's balance? ")
    draught_limit = input("What is your user's over-draught limit.? ")
    Customer(first_name, last_name, user_title, preferred_pronouns, date, user_occupation, user_balance, draught_limit)


main_menu()
