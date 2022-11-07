from customer_class import Customer
import datetime
import csv


def select_customer_by_id():
    id_to_select = input("please enter the ID of the account you would like to manipulate.")

    stop = False
    while stop is False:
        with open('UserDetails.csv', 'r') as file:
            filecontent = csv.reader(file)
            for row in filecontent:
                if row[0] == id_to_select:
                    row_of_values=row
                    stop = True
            if stop is False:
                id_to_select = input("input invalid please try again")

    return id_to_select


def main_menu():
    """creates an infinite loop that presents the user with a list of options for interacting with an account?"""
    stop = False
    while stop is False:
        print("would you like to add a new customer (1), delete a customer (2), edit a customers details(3),"
              " view a list of all customers(4), search for a client(5), deposit some money for a customer(6),"
              " withdraw some money for a customer(7) or logout (8)")
        choice = str(input())
        if choice == "1":
            create_new_account()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            edit_customer()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            search_for_clients_main()
        elif choice == "6":
            make_deposit()
        elif choice=="7":
            make_withdrawal()
        elif choice == "8":
            stop = True
        else:
            print("unexpected input, please try again")


def make_withdrawal():
    customer_id = select_customer_by_id()
    money_to_withdraw = input("how much money would you like to withdraw? ")
    stop = False
    while stop is False:
        try:
            money_to_withdraw = float(money_to_withdraw)
            money_to_withdraw = round(money_to_withdraw,2)
            stop = True
        except:
            money_to_withdraw = input("Invalid input, please try again ")
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == customer_id:
                row_of_values=row
    new_customer= Customer(row_of_values[0], row_of_values[1], row_of_values[2], row_of_values[3], row_of_values[4], row_of_values[5], row_of_values[6], row_of_values[7], row_of_values[8])
    new_customer.withdrawal(money_to_withdraw)
    remove_customer(customer_id)
    new_customer.add_client_to_csv()


def make_deposit():
    customer_id = select_customer_by_id()
    money_to_deposit = input("how much money would you like to deposit? ")
    stop = False
    while stop is False:
        try:
            money_to_deposit = float(money_to_deposit)
            money_to_deposit = round(money_to_deposit,2)
            stop = True
        except:
            money_to_deposit = input("Invalid input, please try again ")
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == customer_id:
                row_of_values=row
    new_customer= Customer(row_of_values[0], row_of_values[1], row_of_values[2], row_of_values[3], row_of_values[4], row_of_values[5], row_of_values[6], row_of_values[7], row_of_values[8])
    new_customer.deposit(money_to_deposit)
    remove_customer(customer_id)
    new_customer.add_client_to_csv()


def get_date():
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
    return date_of_birth


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
    # Need to add validation for checking the user is over 18
    print("What date was your user born? ")
    date_of_birth = get_date()

    user_occupation = input("What is your user's occupation? ")
    if not isinstance(user_occupation, str):
        raise TypeError("occupation should be string")

    i = True
    while i:
        user_balance = input("What is your user's balance? ")
        try:
            user_balance = float(user_balance)
            i = False
        except:
            print("Incorrect balance entered. Please enter your user's balance again")
            i = True
            user_balance = 1

    i = True
    while i:
        draught_limit = input("What is your user's over-draught limit.? ")
        try:
            draught_limit = float(draught_limit)
            i = False
        except:
            print("Incorrect overdraught limit enterred. Please enter your user's overdraught limit again")
            i = True
            draught_limit = 1

    i = 0
    with open('./UserDetails.csv', 'r') as file:
        file_content = csv.reader(file)
        for row in file_content:
            i = row[0]
    i=i[1:]
    i = int(i)
    i+=1
    id = "b" + str(i)

    new_client = Customer(id, first_name, last_name, user_title, preferred_pronouns, date_of_birth, user_occupation, user_balance,
             draught_limit)
    new_client.add_client_to_csv()


def remove_customer(id_to_delete):
    input_file = open('UserDetails.csv', 'r')
    output_file = open('UserDetailsDelete.csv', 'a', newline='')
    writer = csv.writer(output_file)
    reader = csv.reader(input_file)
    for row in reader:
        if row[0] != id_to_delete:
            writer.writerow(row)
    input_file.close()
    output_file.close()

    f = open("UserDetails.csv", "w+")
    f.close()

    input_file_two = open("UserDetailsDelete.csv", "r")
    reader = csv.reader(input_file_two)
    for row in reader:
        with open('./UserDetails.csv', 'a', newline='') as appender:
            writer_object = csv.writer(appender)
            writer_object.writerow(row)
            appender.close()
    input_file_two.close()

    f = open("UserDetailsDelete.csv", "w+")
    f.truncate()
    f.close()


def delete_customer():
    id_to_delete = select_customer_by_id()
    remove_customer(id_to_delete)


def edit_customer():
    choice =  select_customer_by_id()
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == choice:
                row_of_values=row
                print(row)
                stop = False
                while stop is False:
                    try:
                        column_to_change = input(
                            "would you like to change this user's first name(1), last name(2), title(3), preferred pronouns(4), date of birth(5), occupation(6) or overdraught limit(7)")
                        column_to_change = int(column_to_change)
                        if column_to_change>0 and column_to_change<8:
                            stop = True
                        else:
                            print("please enter a number between 1 and 7")
                            stop = False
                    except:
                         print("please enter an integer value")
                remove_customer(choice)

                print("what is the new value you would like to change this column to? ")
                print(row_of_values)
                if column_to_change == "7":
                    column_to_change+=1
                    print("please enter the new balance for the user")
                    new_value = input()
                elif column_to_change== "5":
                    new_value = get_date
                else:
                    new_value = input("please enter the new value for this user")
                row_of_values[column_to_change]= new_value
                print(row_of_values)
                new_customer=Customer(choice,row_of_values[1],row_of_values[2],row_of_values[3],row_of_values[4],row_of_values[5],row_of_values[6],row_of_values[7],row_of_values[8])
                new_customer.add_client_to_csv()
            else:
                print("we do not currently have an applicant with that id")


def search_for_clients_main():
    stop = False
    while stop is False:
        choice = input(
            "would you like to search for a specific client (1) or search for any client that matches a set of "
            "criteria (2)")
        if choice == "1":
            search_for_clients_specific()
            stop = True
        elif choice == "2":
            search_for_clients_by_criteria()
            stop = True
        else:
            print("input unknown please try again")
            stop = False


def search_for_clients_specific():
    first_or_last_name = input("Please enter the first or last name of the client you would like to view")
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[1] == first_or_last_name:
                print(row)
            elif row[2] == first_or_last_name:
                print(row)
            else:
                print("we do not currently have a client with that name")
    user_entered_id = input("Please enter the ID of the client displayed on the terminal you would like to view")
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == user_entered_id:
                print(row)
            else:
                print("we do not currently have an applicant with that id")


def search_for_clients_by_criteria():
    choice=input("would you like to view clients by balance(1), occupation(2), title(3), or age(4)")
    if choice=="1":
        print("yo")
    elif choice=="2":
        print("yo")
    elif choice=="3":
        print("yo")
    elif choice=="4":
        print("yo")


def view_all_customers():
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            print(row)


main_menu()
