from customer_class import Customer
import datetime
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

    first_name = input("What is the first name of your user? ")
    if not isinstance(first_name, str):
        raise TypeError("Name should be string")

    last_name = input("What is the last name of your user? ")
    if not isinstance(last_name, str):
        raise TypeError("Name should be string")

    user_title = input("What is your user's title? ")
    if not isinstance(user_title, str):
        raise TypeError("title should be string")

    preferred_pronouns = input("What are your user's preferred pronouns? ")
    if not isinstance(first_name, str):
        raise TypeError("Name should be string")

    print("What date was your user born? ")
    i = True
    while i:
        try:
            current_date = datetime.date.today()
            date_entry = input('Enter a date (i.e. dd/mm/yyyy) ')
            day, month, year = map(int, date_entry.split('/'))
            if year < 1903:
                print("please enter a valid year your user is born.")
                print("years must be four digits long")
            elif year > current_date.year:
                print("Please enter a valid year for your user's date of birth")
            else:
                date_of_birth = datetime.date(year, month, day)
                print(date_of_birth)
                i = False
        except ValueError:
            print("Incorrect format, please try again")

    user_occupation = input("What is your user's occupation? ")
    if not isinstance(user_occupation, str):
        raise TypeError("occupation should be string")

    i = True
    while i:
        user_balance = input("What is your user's balance? ")
        try:
            user_balance = float(user_balance)
            i=False
        except:
            print("Incorrect balance enterred. Please enter your user's balance again")
            i=True
            user_balance=1

    i = True
    while i:
        draught_limit = input("What is your user's over-draught limit.? ")
        try:
            draught_limit = float(draught_limit)
            i=False
        except:
            print("Incorrect overdraught limit enterred. Please enter your user's overdraught limit again")
            i = True
            draught_limit  = 1

    Customer(first_name, last_name, user_title, preferred_pronouns, date, user_occupation, user_balance, draught_limit)


main_menu()
