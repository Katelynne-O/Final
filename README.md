Final Project: Expenses Tracker - Py-Mates: Jacey Purpura, Katelynne Olifant

Video Demo : https://youtu.be/TNxc6CAjtTE

Project Overview: 
The Expenses Tracker is a Python-based financial management tool designed to help users log, analyze, and manage their expenses efficiently. By providing a straightforward way to track daily expenditures, this tool ensures that users can monitor their spending habits, categorize expenses, and stay within budget.

Managing finances can be challenging, but with this simple and intuitive expense tracker, users gain a clear understanding of where their money is going. The program is ideal for individuals looking to maintain a personal budget or even small businesses wanting to track operational costs.

Features

1. Expense Logging

Users can input:

The name of an expense

The amount spent

The category of expense (e.g., Food, Home, Fun, Miscellaneous, etc.)

2. Data Storage

All expenses are stored in a CSV file (expenses.csv), making it easy to retrieve and analyze data.

The CSV format allows users to open their expense logs in applications like Microsoft Excel or Google Sheets.

3. Budget Summary & Analysis
The program generates a detailed summary that includes:

Spending by category: Breakdown of where the money is being spent.

Total cost: Sum of all expenses recorded.

Remaining budget: Helps users understand how much they have left for the month.

Recommended daily budget: Based on the number of days left in the month, the program suggests a daily spending limit to help maintain financial discipline.

4. Input Validation
To ensure accurate data entry, the program includes:

Error handling for incorrect data types (e.g., entering letters instead of numbers for amounts).

Category validation to prevent invalid entries.

5. File Operations
The program efficiently reads from and writes to the CSV file.

Ensures that data is not lost between sessions.

6. Simple & User-Friendly Interface
Easy-to-use command-line interface that requires minimal technical knowledge.

Clear instructions to guide the user through each step.

How It Works

Run the Program: Execute the Python script in your terminal or command prompt.

Enter Expense Details:

Type in the name of your expense (e.g., "Groceries").

Input the amount spent (e.g., "50").

Choose a category (e.g., "Food").

Store & Analyze:

The expense is saved in the CSV file.

A budget summary is generated, showing spending breakdowns and recommendations.

Repeat as Needed:

Users can add multiple expenses and view updated summaries at any time.

Use Cases:

The Expenses Tracker can be useful in several scenarios:

Personal Budgeting: Helps individuals track daily spending and stay within financial limits.

Student Expense Management: Students can monitor their monthly expenses on food, entertainment, and rent.

Household Budgeting: Families can keep track of shared expenses and allocate budgets accordingly.

Small Business Expense Tracking: Entrepreneurs and freelancers can use it to log business-related expenses and manage costs effectively.

Installation & Setup

Requirements

Python 3.x

CSV module (comes pre-installed with Python)

How to Install

Clone the Repository:

git clone https://github.com/your-repo-name/expenses-tracker.git

Navigate to the Project Directory:

cd expenses-tracker

Run the Script:

python expenses_tracker.py

Code Explanation
The main components of the script include:

User Input Handling: The script takes inputs from the user and validates them.

File Handling: It reads from and writes to a CSV file to store expense data.

Budget Analysis: The script processes the recorded expenses and provides insights on spending habits.

Error Handling: Ensures smooth execution by catching incorrect inputs and handling exceptions.

Future Enhancements

We plan to expand the functionality of this project with the following updates:

Graphical User Interface (GUI): To make the expense tracker more interactive and visually appealing.

Data Visualization: Implementing charts and graphs to display spending trends.

Multi-User Support: Allowing multiple users to maintain separate expense logs.

Cloud Storage Integration: Enabling data synchronization across devices.

Conclusion
The Expenses Tracker is a simple yet powerful tool for managing finances. Whether you're an individual trying to stay within budget or a small business owner looking to track expenses, this program offers an easy-to-use and effective solution. By storing expense data, analyzing spending habits, and providing budget recommendations, it encourages financial responsibility and better money management.




