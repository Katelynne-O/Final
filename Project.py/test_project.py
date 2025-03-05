#Citation: OpenAI. (2025). ChatGPT (March 4 version) [Large language model]. https://openai.com

#Importing unittest module for testing
import unittest

#Importing os module for file handling
import os

#Importing function from project.py module
from project import get_user_expense, save_expense, display_expense, Expense

#Class created for testing the Expense tracker application
class TestExpenseTracker(unittest.TestCase):

#Function created for testing if an Expense object is correctly created with the expected attributes
    def test_function_1(self):
        """Test that an Expense object is correctly created."""

#Creating an expense instance
        expense = Expense(name="Water", category="Food", amount=10.50)

#Asserting that the objects attributes are correct
        self.assertEqual(expense.name, "Water")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 10.50)

#Function to test that expenses being saved to the file and verifying its contents
    def test_function_2(self):
        """Test saving an expense to a file."""
        expense = Expense(name="Groceries", category="Food", amount=25.00)

#Using a test file instead of modifying real data
        file_path = "test_expenses.csv"

# Saving the expense
        save_expense(expense, file_path)

# Reading the file and verifying the content
        with open(file_path, "r") as f:
            lines = f.readlines()

#Checking if the expected entry is in the file
        self.assertIn("Groceries,Food,25.0\n", lines)

#Cleaning up the test file after execution
        os.remove(file_path)

#Function created to test the displaying of expenses
    def test_function_3(self):
        """Test if display_expense correctly processes a file."""
        file_path = "expenses.csv"
        budget = 1000

#Checking if the display_expenses function runs with no problems
        try:
            display_expense(file_path, budget)
            test_passed = True
        except Exception as e:
            test_passed = False
            print(f"Error during display_expense: {e}")

        self.assertTrue(test_passed)

 #Cleaning up the test file
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()