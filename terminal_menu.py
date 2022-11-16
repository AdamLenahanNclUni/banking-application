from customer_class import Customer
import datetime
import csv


def sort_by_id():
    """this subroutine ensures users are ordered in the csv file from lowest id to highest"""
    # without this subroutine there could be clashing ids as ids are created by taking the last
    # id in the file and adding one to it. This could cause an error as if the last id in the
    # file is not the highest then there is no guarantee the new id will be unique
    list_of_ids = []
    # creating an empty list which will store the ids that need to be sorted
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        next(file)
        # opening a file reader that skips the first row in the file as the first row is always the title row and
        # does not need to be sorted
        for row in filecontent:
            try:
                list_of_ids.append(int(row[0]))

            except:
                break
                # this try except statement tries to add the id on the row to the list, if there is an empty row(which
                # there always will be as there is always an empty row at the end of the file) the except clause
                # breaks out of the for loop
    print(list_of_ids)
    list_of_ids = bubble_sort(list_of_ids)
    print(list_of_ids)
    # using the bubble sort subroutine to sort the list into its correct order. This correct order will be referenced
    # later.
    with open('UserDetails.csv', 'r') as file4:
        filecontent4 = csv.reader(file4)

        for row4 in filecontent4:
            if row4[0] == "id":
                output_file = open('UserDetailsDelete.csv', 'a', newline='')
                writer = csv.writer(output_file)
                writer.writerow(row4)
                output_file.close
    # this file reader finds the title row and moves it into a seperate file before any other values so that
    # it remains at the top of the file and does not become sorted by id.
    for x in list_of_ids:
        print("x=", x)
        with open('UserDetails.csv', 'r') as file2:
            filecontent2 = csv.reader(file2)
            next(file2)
            for row2 in filecontent2:
                print("row2 = ", row2)
                if int(row2[0]) == x:
                    output_file = open('UserDetailsDelete.csv', 'a', newline='')
                    writer = csv.writer(output_file)
                    writer.writerow(row2)
                    output_file.close

    # the above block of code is a writer nested in a reader. It loops through the sorted list of ids and the file
    # containing user entries. It looks for the user entry in the file with the smallest id (ie first one in the
    # list) then it writes it to a second csv file. it repeats this with the second smallest id(ie second in the
    # list) and so on until there is a sorted list of users in the second csv file.

    f = open("UserDetails.csv", "w+")
    f.close()
    # the above code removes all entries in the original file and turns it into an empty csv file.

    with open('UserDetailsDelete.csv', 'r') as file3:
        filecontent3 = csv.reader(file3)
        for row3 in filecontent3:
            output_file = open('UserDetails.csv', 'a', newline='')
            writer = csv.writer(output_file)
            writer.writerow(row3)
            output_file.close

    f = open("UserDetailsDelete.csv", "w+")
    f.close()
    # this code copies all entries in the secod file back into the first and then deletes all entries in the second file.


def bubble_sort(list_of_ids):
    """sorts a list of ids using bubble sort"""
    n = len(list_of_ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_ids[j] > list_of_ids[j + 1]:
                list_of_ids[j], list_of_ids[j + 1] = list_of_ids[j + 1], list_of_ids[j]
    return list_of_ids
    #the above code is a basic bubble sort algorithm


def select_customer_by_id():
    """this subroutine allows the user to enter an id and select a customer by their unique id"""
    view_customer_id_and_name()
    # views a list of all customer ids and their related names
    id_to_select = input("please enter the ID of the account you would like to manipulate.")
    # takes the users input as the id they wish to select
    stop = False
    while stop is False:
        # this while loop is used to keep the user entering ids until they enter a valid id
        with open('UserDetails.csv', 'r') as file:
            filecontent = csv.reader(file)
            for row in filecontent:
                if row[0] == id_to_select:
                    row_of_values = row
                    stop = True
                    print(row)
                    # if there is an entry in the csv file with the same id as the user's input then the value stop
                    # is set to true and the while loop is exited. The user is also shown the full entry that corre-
                    # sponds with the id they enterred.
            if stop is False:
                id_to_select = input("input invalid please try again")
            # if the id the user enters is invalid (ie does not correspond with an entry in the ccsv file) then the
            # user is prompted to enter the id again.
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
        elif choice == "7":
            make_withdrawal()
        elif choice == "8":
            stop = True
        else:
            print("unexpected input, please try again")
            # takes the input of a user and calls the subroutine for the functionality that corresponds with the
            # the users option. If the user's entry is invalid the else statement is tripped and the user is asked
            # to try again. The only way to stop the loop is to press 8 to log out.


def make_withdrawal():
    """this subroutine takes the account and the amount of money the user would like to withdraw, then it calls the
    withdrawal method in the customer class."""
    customer_id = select_customer_by_id()
    # get a valid error checked id from the user using the select_customer_by_id subroutine
    money_to_withdraw = input("how much money would you like to withdraw? ")
    stop = False
    while stop is False:
        try:
            money_to_withdraw = float(money_to_withdraw)
            money_to_withdraw = round(money_to_withdraw, 2)
            stop = True
        except:
            money_to_withdraw = input("Invalid input, please try again ")
            # the above try except statement attempts to take the user's input and convert it to a
            # float with two decimal places. If that fails then the user is asked to enter the
            # amount of money they would like to withdraw again. Due to the while loop this process
            # is repeated until a valid amount of money to withdraw is entered.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == customer_id:
                # a file reader is opened and the account the user has previously selected is read to row_of_values
                row_of_values = row
    new_customer = Customer(row_of_values[0], row_of_values[1], row_of_values[2], row_of_values[3], row_of_values[4],
                            row_of_values[5], row_of_values[6], row_of_values[7], row_of_values[8])
    # the row of values the user has selected is instantiated into an object.
    new_customer.withdrawal(money_to_withdraw)
    # the values in the object are updated.
    remove_customer(customer_id)
    # the values in the csv file are not updated along with the object so they are removed.
    new_customer.add_client_to_csv()
    # the object is now added to the csv file in order to save it
    sort_by_id()
    # the csv file is sorted to prevent clashing ids later on in the program


def make_deposit():
    """this subroutine takes the account and the amount of money the user would like to deposit, then it calls the
        deposit method in the customer class."""
    customer_id = select_customer_by_id()
    money_to_deposit = input("how much money would you like to deposit? ")
    # get a valid error checked id from the user using the select_customer_by_id subroutine
    # the money the user would like to deposit is taken from the user to.
    stop = False
    while stop is False:
        try:
            money_to_deposit = float(money_to_deposit)
            money_to_deposit = round(money_to_deposit, 2)
            stop = True
        except:
            money_to_deposit = input("Invalid input, please try again ")
            # the above try except statement attempts to take the user's input and convert it to a
            # float with two decimal places. If that fails then the user is asked to enter the
            # amount of money they would like to deposit again. Due to the while loop this process
            # is repeated until a valid amount of money to deposit is entered.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == customer_id:
                # a file reader is opened and the account the user has previously selected is read to row_of_values
                row_of_values = row
    new_customer = Customer(row_of_values[0], row_of_values[1], row_of_values[2], row_of_values[3], row_of_values[4],
                            row_of_values[5], row_of_values[6], row_of_values[7], row_of_values[8])
    # the row of values the user has selected is instantiated into an object.
    new_customer.deposit(money_to_deposit)
    # the values in the object are updated.
    remove_customer(customer_id)
    # the values in the csv file are not updated along with the object so they are removed.
    new_customer.add_client_to_csv()
    # the object is now added to the csv file in order to save it
    sort_by_id()
    # the csv file is sorted to prevent clashing ids later on in the program


def get_date():
    """this subroutine gets the user to enter a single valid error checked date."""
    # there is no validation to check if the user is over 18 in this subroutine as it is assumend children can hold
    # bank accounts (child trust funds etc)
    i = True
    while i:
        try:
            current_date = datetime.date.today()
            date_entry = input('Enter a date (i.e. dd/mm/yyyy) ')
            day, month, year = map(int, date_entry.split('/'))
            # the user is asked to enter a date in dd/mm/yyyy format which is then split into constituent date,
            # month and year parts
            if year < 1903:
                print("please enter a valid year your user is born.")
                print("years must be four digits long")
                # if the year enterred is greater than the worlds oldest person the user is asked to enter another
                # valid date
            elif datetime.date(year, month, day) > current_date:
                print("Please enter a valid year for your user's date of birth")
                # if the user enters a date that is in the future they are asked to try again
            else:
                date_of_birth = datetime.date(year, month, day)
                print(date_of_birth)
                i = False
                # if the user enters a valid date then the while loop is exited and their date is saved in date-time
                # format
        except ValueError:
            print("Incorrect format, please try again")
            # if the user enters an incorrect data type then they are asked to try again
    return date_of_birth


def create_new_account():
    """gives the user a way to create a new line in the csv file which represents a user"""

    first_name = input("What is the first name of your user? ")
    if not isinstance(first_name, str):
        raise TypeError("Name should be string")
    # takes a first name off the user and raises an error if it isn't a string

    last_name = input("What is the last name of your user? ")
    if not isinstance(last_name, str):
        raise TypeError("Name should be string")
    # takes a last name off the user and raises an error if it isn't a string
    user_title = input("What is your user's title? ")
    if not isinstance(user_title, str):
        raise TypeError("title should be string")
    # takes a title off the user and raises an error if it isn't a string
    preferred_pronouns = input("What are your user's preferred pronouns? ")
    if not isinstance(first_name, str):
        raise TypeError("preferred pronouns should be a string")
    # # takes a set of prefered pronouns off the user and raises an error if it isn't a string
    print("What date was your user born? ")
    date_of_birth = get_date()
    # calls the get_date subroutine to get a valid date of birth for the user.
    user_occupation = input("What is your user's occupation? ")
    if not isinstance(user_occupation, str):
        raise TypeError("occupation should be string")
    # takes an occupation off the user and raises an error if it isn't a string
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
    # the above while loop takes the users balance, checks to see if its a float value and if it isn't gets the user
    # to enter it again.

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
            # the above while loop takes the users overdraught limit, checks to see if its a float value and if it
            # isn't gets the user to enter it again.

    i = 0
    with open('./UserDetails.csv', 'r') as file:
        file_content = csv.reader(file)
        for row in file_content:
            i = row[0]
    i = int(i)
    i += 1
    id = str(i)
    # this line generates the id for the users csv file by selecting the id of the last entry and creating an id that is greater than it by one
    new_client = Customer(id, first_name, last_name, user_title, preferred_pronouns, date_of_birth, user_occupation,
                          user_balance,
                          draught_limit)
    new_client.add_client_to_csv()
    # the above two lines of code create a new object which is then added to the csv file.
    sort_by_id()
    # the csv file is sorted.


def remove_customer(id_to_delete):
    """this subroutine takes an argument(which is the id of a user) and deletes the corresponding row from the csv file"""
    input_file = open('UserDetails.csv', 'r')
    output_file = open('UserDetailsDelete.csv', 'a', newline='')
    writer = csv.writer(output_file)
    reader = csv.reader(input_file)
    for row in reader:
        if row[0] != id_to_delete:
            writer.writerow(row)
    input_file.close()
    output_file.close()
    # reading every row in the csv file which contains the value we are deleteing. If it doesn't have the
    # id_to_delete in it we write it to the next row. If it does we don't.

    f = open("UserDetails.csv", "w+")
    f.close()
    # removing every value from the original file.
    input_file_two = open("UserDetailsDelete.csv", "r")
    reader = csv.reader(input_file_two)
    for row in reader:
        with open('./UserDetails.csv', 'a', newline='') as appender:
            writer_object = csv.writer(appender)
            writer_object.writerow(row)
            appender.close()
    input_file_two.close()
    # rewriting the values in the second file back into the origianl. because the row we were looking to delete was
    # not copied over the first time we did this the original csv file contains all of the same rows as before i the
    # same order with the exception of the mrow we did not copy over
    f = open("UserDetailsDelete.csv", "w+")
    f.truncate()
    f.close()
    # deleting all the values in the file we copied our original file to.
    sort_by_id()
    # the csv file is sorted


def delete_customer():
    """this subroutine deletes a row from the csv file"""
    id_to_delete = select_customer_by_id()
    remove_customer(id_to_delete)
    # two subroutines are used to make this subroutine. this is to prevent code duplicates.


def edit_customer():
    """this subroutine allows the user to edit part of a row in the csv file"""
    found_specified_user = False
    choice = select_customer_by_id()
    # get the id of a user which we will be editing.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        next(file)
        # open a file reader and skip the first row. This is to avoid the title row which is always the first row.
        for row in filecontent:
            row = list(row)
            # looping through each row.
            if row[0] == choice:
                #checking to see if the current row is the user we are looking for
                row_of_values = row
                stop = False
                found_specified_user = True
                while stop is False:
                    try:
                        column_to_change = input(
                            "would you like to change this user's first name(1), last name(2), title(3), preferred pronouns(4), date of birth(5), occupation(6) or overdraught limit(7)")
                        column_to_change = int(column_to_change)
                        # take the users input and ask which column they would like to change.
                        if column_to_change > 0 and column_to_change < 8:
                            stop = True
                            # if the user enters a valid column let them exit the while loop
                        else:
                            print("please enter a number between 1 and 7")
                            stop = False
                            # if the user doesn't enter a valid don't let them leave and ask
                            # them what they would like to select again
                    except:
                        print("please enter an integer value")
                remove_customer(choice)
                # remove the old values of the user from the csv file

                if column_to_change == 7:
                    column_to_change += 1
                    # if the user wants to change the overdraught limit then increment column to change by 1 as the
                    # index calue of overdraught limit is 8 and is referenced by column to change later on.
                    stop = False
                    while stop == False:
                        try:
                            new_value = input("please enter the new overdraught limit for the user")
                            new_value = float(new_value)
                            stop = True
                            # the user is asked to enter the new overdraught limit. If they enter a valid float value they
                            # are allowed to exit the while loop
                        except:
                            print("input formatted incorrectly, please try again")
                elif column_to_change == 5:
                    new_value = get_date()
                    # because date is in datetime format we call getdate() to ensure the date
                    # the user enters is valid and error free
                else:
                    new_value = input("please enter the new value for this user")
                row_of_values[column_to_change] = new_value
                # if the user enters a valid column which accepts a string value then we
                # simply update the users value with an equals statement
                print(row_of_values)
                new_customer = Customer(choice, row_of_values[1], row_of_values[2], row_of_values[3], row_of_values[4],
                                        row_of_values[5], row_of_values[6], row_of_values[7], row_of_values[8])
                new_customer.add_client_to_csv()
                # the new values for user are instantiated into an object and added to the csv file
                break
        if not found_specified_user:
            print("we do not currently have an applicant with that id")
            #if we can't find the user the id entered corresponds to  we print this statement
    sort_by_id()
    #the csv file is sorted.


def search_for_clients_main():
    """this subroutine gets the user to decide whether they want to search for clients using a first name, last name,
    date of birth or negative balance. """
    stop = False
    while stop is False:
        choice = input(
            "would you like to search for a specific client by first name(1), "
            "by last name(2) by birthday(3) or by negative balance criteria (4)")
        if choice == "1":
            search_for_clients_first_name()
            stop = True
        elif choice == "2":
            search_for_clients_by_last_name()
            stop = True
        elif choice == "3":
            search_for_clients_by_birthday()
            stop = True
        elif choice == "4":
            search_for_clients_by_negative_balance()
            stop = True
        else:
            print("input unknown please try again")
            stop = False
        # this while loop ends once the user enters a valid choice (ie 1,2,3 or 4) otherwise it keeps asking the user
        # which criteria they want to search the csv file with. it uses an if statment to check the users input and
        # subroutine calls to fetch the functionality the user wants to interact with.


def search_for_clients_first_name():
    """this subroutine gets the user to enter a last name and then prints out a list of all clients with that last
        name """
    first_name = input("Please enter the first name of the client you would like to view")
    count = 0
    # we get the user to enter a first name and initialise the variable count to be equal to 0
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[1] == first_name:
                print(row)
                count += 1
                # we read through every entry in the file and if the first name column matches the value entered
                # by the user we print that row and increment count by one.
        if count > 0:
            select_customer_by_id()
            # if count>0 (ie if we have found one or more users with the first name entered) then we get the user
            # to select a specific client
        else:
            print("no users found with the provided data")
            # if there are no users with the first name entered then we tell the user this by using a print statement.


def search_for_clients_by_last_name():
    """this subroutine gets the user to enter a first name and then prints out a list of all clients with that first
    name """
    count = 0
    last_name = input("Please enter the last name of the client you would like to view")
    # we get the user to enter a last name and initialise the variable count to be equal to 0
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[2] == last_name:
                print(row)
                count += 1
                # we read through every entry in the file and if the last name column matches the value entered
                # by the user we print that row and increment count by one.
        if count > 0:
            print("please enter the id of the client you would like to view from this list")
            select_customer_by_id()
            # if count>0 (ie if we have found one or more users with the last name entered) then we get the user
            # to select a specific client
        else:
            print("no users found with the provided data")
            # if there are no users with the last name entered then we tell the user this by using a print statement.


def search_for_clients_by_birthday():
    """this subroutine gets a user to enter a date of birth, it then searches
    the csv file to find all the users with a atching date of birth"""
    count = 0
    date_of_birth = get_date()
    # we get the user to enter a date and initialise the variable count to be equal to 0
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if str(row[5]) == str(date_of_birth):
                print(row)
                count += 1
                # we read through every entry in the file and if the date of birth column matches the value entered
                # by the user we print that row and increment count by one.
        if count > 0:
            print("please enter the id of the client you would like to view from this list")
            select_customer_by_id()
            # if count>0 (ie if we have found one or more users with the date of birth entered) then we get the user
            # to select a specific client
        else:
            print("no users found with the provided data")
            # if there are no users with the date of birth enered then we tell the user this by using a print statement.


def search_for_clients_by_negative_balance():
    """this csv file prints a list of all users with a negative balance"""
    count = 0
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            try:
                compare = float(row[7])
                if compare < 0:
                    print(row)
                    count += 1
            except:
                count += 0
                # reads every 8th column in all the rows in the table. If there are any with a value less than 0 they
                # are printed to the screen and the count is incremented by one.
        if count > 0:
            print("please enter the id of the client you would like to view from this list")
            select_customer_by_id()
            # if there are users with a balance less than 0 the user is presented with a list of them and asked to
            # select one.
        else:
            print("no users found with the provided data")
            # if there are no users with a balance of less than 0 then the user is told this with a print statement


def view_all_customers():
    """this subroutine prints a list of all columns of everyone in the userDetails csv file"""
    # code adapted from https://www.tutorialspoint.com/how-to-read-csv-file-in-python#:~:text=Explanation%20line%20by
    # %20line%201%20import%20csv%20%E2%88%92,filecontents%20to%20print%20the%20file%20content%20row%20wise.
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            print(row)
            # opens a file reader and prints everything in the csv file


def view_customer_id_and_name():
    """this subroutine prints a list of all ids names and lastnames of everyone in the userDetails csv file"""
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            print(row[0], row[1], row[2])
            # opens a file reader and prints a list of the first names, last names and ids of everone in the csv file

sort_by_id()
main_menu()
