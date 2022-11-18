from customer_class import Customer
import csv
# Due to bad seperation of concerns testing can only be performed on some methods in this program. While all the methods
# work in the terminal menu I cannot test them with hard code. The parts of the program I can test are tested here.
# For information on how to check if the terminal menu works please check the readme file for instructions on its usage.


def test_add_client_to_csv():
    id_to_select = "101"
    found = False
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == id_to_select:
                print(row)
                found = True
        if found == False:
            print("there are currently no user's with that id")


def test_withdrawal():
    id_to_select = "101"
    found = False
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == id_to_select:
                print(row[7])
                found = True
        if found == False:
            print("there are currently no user's with that id")


def test_deposit():
    id_to_select = "101"
    found = False
    with open('UserDetails.csv', 'r') as file:
        filecontent = csv.reader(file)
        for row in filecontent:
            if row[0] == id_to_select:
                print(row[7])
                found = True
        if found == False:
            print("there are currently no user's with that id")


def reset_file():
    input_file = open('UserDetails.csv', 'r')
    output_file = open('UserDetailsDelete.csv', 'a', newline='')
    writer = csv.writer(output_file)
    reader = csv.reader(input_file)
    for row in reader:
        if row[0] != "101":
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
    # rewriting the values in the second file back into the original. because the row we were looking to delete was
    # not copied over the first time we did this the original csv file contains all of the same rows as before i the
    # same order with the exception of the row we did not copy over
    f = open("UserDetailsDelete.csv", "w+")
    f.truncate()
    f.close()
    # deleting all the values in the file we copied our original file to.
    # this subroutine deletes the test user from the database. It is run at the end of the tests to reset the file
    # so that tests can be run multiple times without having a user with more than one of the same id.

# this test shows that the add client to csv method works
test_add_client_to_csv()
# this test should print out "there are currently no user's with that id" at this stage
new_customer = Customer("101","Amandie","Tearney","Dr","she/her","1999-08-31","Chief Design Engineer","-752.53","991.48")
Customer.add_client_to_csv(new_customer)
test_add_client_to_csv()
# this test should print out "['101', 'Amandie', 'Tearney', 'Dr', 'she/her', '1999-08-31', 'Chief Design Engineer',
# '-752.53', '991.48']" at this stage.

# this test tests that the withdrawal method works
test_withdrawal()
# this test should print "-752.53" at this stage
# "current amount in bank balance is  -752.53"
new_customer.withdrawal(100)
# "you've withdrawn money and gone into your overdraft, you are still within the limit though"
# "new amount in bank balance is  -852.53"
reset_file()
# this is done to delete the old user details from the file which are out of date.
Customer.add_client_to_csv(new_customer)
#this is done to save the new details to the csv file for later use.
test_withdrawal()
#this should print "-852.53"

test_deposit()
#this test should print the users current balance which is unchanged from last time
# this test proves that the new user details have been saved to the file.
reset_file()
# this subroutine removes old outdated user information from the file
new_customer.deposit(100)
# this test tests that the deposit method works
# the program should write "you have deposited £ 100.0 new bank balance is £ -752.53" to the terminal
Customer.add_client_to_csv(new_customer)
# this saves the new user info to the file to be read at a later time
test_deposit()
# the program should write "-752.53" to the terminal



# this test tests that the string representation of the user is implemented correctly
print(new_customer.__str__())
# should print "Customer Amandie Tearney has a balance of -752.53"

# this test tests the __repr__ method works correctly.
print(new_customer.__repr__())
# should print "Customer Dr Amandie Tearney has a balance of -752.53 their overdraught limit is 991.48.
# They were born on -752.53. Their pronouns are she/her and they are a Chief Design Engineer"


reset_file()
# this line of code resets the file so the tests can be run multiple times
