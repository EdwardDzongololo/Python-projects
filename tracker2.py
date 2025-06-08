import csv
from datetime import datetime
import os 

# Check if the expenses file exists  
# If not, create it with CSV headers (Date, Category, Amount, Description) 
filename= "Expenses2.csv"
if not os.path.exists(filename):
    with open (filename, "w", newline="")as file:
        writer= csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Descrition"])

# Display menu options in a loop until user exits: 
def add_new_expense(filename):
        print("\nAdd  Expense New")
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter category: ")
        amount = float (input ("Enter amount: "))
        description = input("Enter description: ")
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description]) 
while True:
    print("1. Add Expense:  ") 
    print("2. View Expenses: ")
    print("3. Exit  ")
    # Get user input for menu choice
    choice= input("Enter your choice (1-3):")
    
    # Call the appropriate function based on choice 
    if choice== "1":
        add_new_expense(filename)
    elif choice== "2":
        view_all_expenses(filename)
    elif choice  == "3":
        print("Exiting the program. Goodbye!")  
        break
    # Handle invalid inputs gracefully   
    
