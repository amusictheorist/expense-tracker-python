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

