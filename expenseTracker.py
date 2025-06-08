import csv
from datetime import datetime
import os

def main():
    filename = "expenses.csv"
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
           
    while True: 
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_expense(filename)
        elif choice == "2":
            view_expenses(filename)
        elif choice == "3":
            print("Goodbye!")
            break   
        else: 
            print("Invalid choice, please try again")
              
def add_expense(filename):
    print("\nAdd New Expense") 
    date = datetime.now().strftime("%Y-%m-%d") 
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")  # Added confirmation
 
def view_expenses(filename):
    print("\nAll Expenses")  
    print("-"*60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':>10} | Description")         
    print("-"*60)  
    
    total = 0.0
    
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file) 
            next(reader)  # Skip header
            
            for row in reader:
                if not row: 
                    continue  
                date, category, amount, desc = row
                print(f"{date:<12} | {category:<15} | ${float(amount):>9.2f} | {desc}")
                total += float(amount)
                
        print("-" * 60)
        print(f"Total Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet!")    
        
if __name__ == "__main__":
    main()