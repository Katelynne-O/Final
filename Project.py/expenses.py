#A class named Expense to represent an expense item with the name, category, and amount.
class Expense:

#Function created to initialise an expense object
    def __init__(self, name, category, amount) -> None:

#Variable created to store the name of an expense
        self.name = name

#Variable created to store the category of the expense
        self.category = category

#Variable created to store the price of the expense
        self.amount = amount
    
#Returning a string representation of the expense object
    def __repr__(self):

#returning a formatted string with the details of the expense
        return f"<Expense: {self.name},{self.category}, ${self.amount: .2f}>"