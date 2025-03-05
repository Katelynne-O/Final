#Citation: OpenAI. (2025). ChatGPT (March 4 version) [Large language model]. https://openai.com

#Importing datetime module to help execute date and time related tasks
import datetime
#Importing the calendar module to help execute month to month calculations
import calendar
#Importing List from the typing module for type hinting
from typing import List
#Importing the Expense from the expenses module created
from expenses import Expense


def main():
    print ("Running Tracker: ")

    #File where the expenses are saved
    expense_file_path = "expenses.csv"
    
    #Set budget for users every month
    budget = 2000

    # Get user to input their expense
    expense = get_user_expense()
    print (expense)
    
    #write their expense to a file
    save_expense(expense, expense_file_path)


    # read the file and summarize expenses
    display_expense(expense_file_path, budget)
    

def get_user_expense():
    
#Get User input for the name of the expense and amount
    name_expense = input("Enter expense name: ")
    amount_expense = float(input("Enter expense amount: "))

#Setting a predefined list of options for the category of the expense: Food, Home, Fun and Miscelennous
    categories_expense = [
       "Food", 
       "Home", 
       "Fun" , 
       "Miscelennous",
       ]

#Loop until a valid category is selected 
    while True:
       print("Select a category: ")

#Displaying available categories
       for i, category_name in enumerate(categories_expense):
          print(f"{i+1}. {category_name}")
        
#Getting the user's selection   
       value_range = f"[1 - {len(categories_expense)}]"
       selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

#Validating the selection made by the user
       if selected_index in range(len(categories_expense)):
          selected_category = categories_expense[selected_index]

#Creating an Expenses object with the user's input
          new_expense = Expense(name = name_expense, category = selected_category, amount = amount_expense )
          return new_expense
       else:
          print("Invalid Category. Please try again")
          
          
#Function made to save the expenses into a CSV file     
def save_expense(expense: Expense, expense_file_path):

#Opening the file in append mode and writing the expense details to the file
    with open (expense_file_path, "a") as f:
       f.write(f"{expense.name},{expense.category},{expense.amount}\n")
   
#Function made to retrieve the expenses from the file and display expenses, remaining budget
#and a proposed daily budget
def display_expense(expense_file_path, budget):

#List created to store expense objects from the file
    expenses: List[Expense] = []

#Reading the expenses from the CSV file created (expenses.csv)
    with open(expense_file_path, "r") as f:
       lines = f.readlines()
       for line in lines:
          stripped_line = line.strip()
          expense_name, expense_category,expense_amount = stripped_line.split(",")

#Converting the String values into an Expense object
          line_expenses = Expense(name = expense_name, amount = float(expense_amount), category = expense_category,)

#Appending the list
          expenses.append(line_expenses)

#Creating a dictionary to categorize expenses          
    amount_by_category = {}
    for expense in expenses:
       key = expense.category
       if key in amount_by_category:
          amount_by_category[key] += expense.amount
       else:
          amount_by_category[key] = expense.amount

#Displaying categorized expenses  
    print(red("Expenses By Category: "))   
    for key , amount in amount_by_category.items():
       print(red(f"{key}: ${amount:.2f}"))

#Calculating and displaying the total amount of expenses spent for the month
    total_spent = sum([x.amount for x in expenses])
    print(green(f"The total you've spent this month is: ${total_spent:.2f} "))

#Calculating and displaying the remaining budget for the month
    remaining_budget = budget - total_spent
    print (green(f"Budget Reamining for this month: ${remaining_budget:.2f} "))

#Getting the current date
    now = datetime.datetime.now()

#Calculating in the total amount of days in the current month
    days_in_the_month = calendar.monthrange(now.year, now.month)[1]

#Calculating the remaining days left in the current month
    remaining_days_in_month = days_in_the_month - now.day

#Displaying the remaining days in green
    print(green(f"Remaining days in the current month: {remaining_days_in_month} days"))

#Calculating the suggested daily budget for the rest of the month
    daily_budget = remaining_budget/remaining_days_in_month

#Displaying the suggest daily budget in purple
    print(purple(f"Suggested budget per day: ${daily_budget:.2f}"))

#Functions for formatting the colour of the texts
def green(var):
   return f"\033[92m{var}\033[0m"  

def red(text):
    return f"\033[91m{text}\033[0m"  

def purple(text):
    return f"\033[95m{text}\033[0m"

#Running the main function if the script is executed directly
if __name__ == "__main__":
 main()