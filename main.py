class Customer:
    """A class created to make a blueprint for customers of the bank"""
    def __init__(self, firstName, lastName, title, preferredPronouns, dateBorn, occupation, balance, overdraftLimit):
        #initialising attributes for the class
        self.f = firstName
        self.l = lastName
        self.t = title
        self.p = preferredPronouns
        self.d = dateBorn
        self.o = occupation
        self.b = balance
        self.ov = overdraftLimit



