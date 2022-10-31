import csv
class Customer:
    """A class created to make a blueprint for customers of the bank"""

    def __init__(self, first_name, last_name, title, preferred_pronouns, date_born, occupation, balance, overdraft_limit):
        """creates a user entity and adds them to the csv file for later use"""
        # initialising attributes for the class
        self.f = first_name
        self.l = last_name
        self.t = title
        self.p = preferred_pronouns
        self.d = date_born
        self.o = occupation
        self.b = balance
        self.ov = overdraft_limit

        i = 0
        with open('./UserDetails.csv', 'r') as file:
            file_content = csv.reader(file)
            for row in file_content:
                i += 1
        id = "b"+str(i)

        row_of_items = [id, self.f, self.l, self.t, self.p, self.d, self.o, self.b, self.ov]

        with open('./UserDetails.csv', 'a',  newline='') as appender:
            writer_object = csv.writer(appender)
            writer_object.writerow(row_of_items)
            appender.close()

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

