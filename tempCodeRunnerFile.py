import csv
import os

def add_expense(filename, date, category, amount, description):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        writer.writerow([date, category, amount, description])

# Example usage:
add_expense('expenses.csv', '2024-06-01', 'Food', 12.50, 'Lunch')