Banking application for assessment 2
===================================
Overview of the program
-----------------------
This application uses object oriented programming along with a procedural terminal interface allow the user to act
as an administrator for a bank. This means that the user is allowed access to all accounts to edit, make deposits
and make withdrawals as they see fit alongside creating and deleteing new accounts. Account details are stored in a
csv file for later use.

Users are allowed to query the csv file to search for specific users. When editing user's details (eg making a deposit
to change their balance) the row representing the user is saved to an object and changes are made in an object oriented
manner.

Assumptions
-----------
It is assumed that no two people will share an id.

It is assumed that the user will not deliberately try and break the program by entering "id" when making changes to users

It is assumed that a user can be created with a negative amount of money in their bank account.

It is assumed that when searching for a user capitalisation matters ie if "adam" is entered "Adam" will not be equal to it.
(ie the program is case-sensitive when searching)

It is assumed that the user will not enter a negative number for the withdrawal or deposit options for the program.

Due to the way accounts were generated only 2 users have a negative balance. The unusually low number of clients in
their overdraught is not a bug it is just due to the way the data was generated on mockaroo.

How to run
----------
type "pip install -r requirements.txt" into the terminal

type "python tests.py" to run the tests

type "python terminal_menu.py" in the terminal. Follow the instructions as they come up to complete the tasks you want
to complete.

PLEASE RUN TESTS BEFORE ADDING USERS. THE ID VALUE FOR THE TEST USER IS HARD CODED AS 101. ADDING A NEW USER BEFORE 
RUNNING TESTS WILL CAUSE TESTS TO FAIL DUE TO CLASHING ID'S (also the tests.py file does not test the whole
functionality of the project due to bad separation of front end and back end. All purely back end methods are tested but
front end subroutines can't be tested. To test whether the parts of the program not covered in tests.py work please use
the terminal menu as directed in the specific use case)

Specific Use Case
----------------
open the terminal menu as discussed in the "how to run" section of this file. Wait for the program to load. Select an
option from the main menu.

If you enter 1 you will be required to enter the user's first name, last name, title, preferred
pronouns, date of birth, occupation, current balance and over-draught limit. Once this is done (provided all data is entered
correctly) an id will be generated for the user and the user will be added to the csv file. If at any point you enter
invalid data eg ("aaa" for date of birth) you will be asked to try again until you enter valid data.

If you enter 2 you will be presented with a list of all the first names, last names and Ids of the users in the csv file.
You will then be asked to enter the id that corresponds to the user you want to delete. If you enter a valid id then you
will be presented with a list of all the users still in the csv file and the user with the id you entered will be deleted.
If you enter an invalid id then the program will print that the id is invalid and will ask you to try again until
you enter a valid id.

If you enter 3 in the main menu then you will be presented with a list of all the ids first names and last names of the
users in the csv file. You will then be asked to select one (if the selection is valid you will move past this stage, if
not then you will be asked to enter your selection again until it isn't invalid). Once you have selected a user you will
be shown a list of all their details and asked whether you would like to change their first name, last name, title, preferred,
pronouns, date of birth, occupation or overdraught limit. overdraught limit only accepts float values and date of birth
requires a valid date to be entered. Everything else accepts any string of any length.

If you enter 4 then you will be presented with a list of all the customers in the csv file and returned to the main menu.

If you enter 5 you will be asked whether you want to search for clients by first name, last name, birthday or negative balance.
if you choose negative balance then a list of all users is displayed with a balance of less than 0. If you choose anything
else you will be asked to enter the value you would like to search the csv file for. Once entered the program searches
the csv file for the value. If it finds it, it prints out all the rows that contain it. If it doesn't it prints out an
error message letting the user know there are no rows with that value in the csv file.

If you enter 6 you will be presented with a list of the id, the first name, and the last name of everyone in the csv file.
You will then be asked to select someone to add money to. Once you have selected someone you will be presented with a list
of all their details. You will then be asked how much money you would like to deposit. after entering a valid amount that
money will be added to the user's balance

If you enter 7 you will be presented with a list of the id, the first name, and the last name of everyone in the csv file.
You will then be asked to select someone to withdraw money from to. Once you have selected someone you will be presented
with a listof all their details. You will then be asked how much money you would like to withdraw. after entering a valid
amount that money will be removed to the user's balance

Pressing 8 will end the program.