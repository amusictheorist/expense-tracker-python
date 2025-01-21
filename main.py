import json
from datetime import datetime

def load_data():
  try:
    with open('data.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return {'expenses': [], 'budgets': {}}
  
def save_data(data):
  with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

def add_expense(data, amount, category, date=None, description=''):
  if not date:
    date = datetime.now().strftime('%Y-%m-%d')
  expense = {
    'amount': amount,
    'category': category,
    'date': date,
    'decription': description
  }
  data['expenses'].append(expense)
  save_data(data)
  print(f"Expense of {amount} added in category '{category}'.")

def view_expenses(data):
  if not data['expenses']:
    print('No expenses recorded yet.')
    return
  for exp in data['expenses']:
    print(f"Date: {exp['date']} | Amount: {exp['amount']} | Category: {exp['category']} | Description: {exp['description']}")

def view_budget(data):
  print('\nCurrent Budgets:')
  for category, budget in data['budgets'].items():
    category_expenses = sum(exp['amount'] for exp in data['expenses'] if exp['category'] == category)
    remaining_budget = budget - category_expenses
    print(f'{category.capitalize()}: Budgeted: {budget}, Spent: {category_expenses}, Remaining: {remaining_budget}')

def update_budget(data, category, new_budget):
  data['budgets'][category] = new_budget
  save_data(data)
  print(f'Budget for {category} updated to {new_budget}.')

