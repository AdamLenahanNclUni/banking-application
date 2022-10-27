from customer_class import Customer


def main_menu():
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
    Customer(" ", " ", " ", " ", " ", " ", " ", " ")


main_menu()
