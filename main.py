import csv
class Customer:
    """A class created to make a blueprint for customers of the bank"""

    def __init__(self, firstName, lastName, title, preferredPronouns, dateBorn, occupation, balance, overdraftLimit):
        # initialising attributes for the class
        self.f = firstName
        self.l = lastName
        self.t = title
        self.p = preferredPronouns
        self.d = dateBorn
        self.o = occupation
        self.b = balance
        self.ov = overdraftLimit



    def withdrawal(self, amount):
        """lets the user withdraw an amount of money, catches any errors caused by going over overdraft limit"""
        print("current amount in bank balance is ", self.b)
        if amount < self.b:
            self.b -= amount
            print("withdrawing some money")
            # if the user withdraws money they have in their account
            # then the money is simply deducted from their account
        elif amount > self.b:
            # if the user withdraws more money than they have in their
            # account then a check is performed to make sure they
            # haven't gone over their overdraft limit
            if self.b - amount > -self.ov:
                self.b -= amount
                print("you've withdrawn money and gone into your overdraft, you are still within the limit though")
            else:
                self.b -= amount
                self.b -= 5
                print("you've withdrawn some money and gone into your overdraft")
        print("new amount in bank balance is ", self.b)

    def deposit(self, amount):
        """lets the user deposit an amount of money, adds it to their account"""
        self.b += amount
        print("you have deposited £", amount, "new bank balance is £", self.b)


def addUser():
    print("adding User")

def searchForUser():
    print("searching for user")

def withdrawForUser():
    print("withdraw for user")

def depositForUser():
    print("deposit for user")

