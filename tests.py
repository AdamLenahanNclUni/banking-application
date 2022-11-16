from customer_class import Customer
# test making withdrawals, making deposits
# the subroutine below is a copy of the make withdrawal subroutine from the terminal menu file.
# a slight difference has been made to this subroutine as all user input values have been hard coded
# so testing runs automatically

def make_withdrawal_1():
    customer_id = "b1"
    # get a valid error checked id from the user using the select_customer_by_id subroutine
    money_to_withdraw = 100
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