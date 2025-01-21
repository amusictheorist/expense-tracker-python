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

def main():
  data = load_data()

  while True:
    print('\n--- Expense Tracker CLI ---')
    print('1. Add expense')
    print('2. View expenses')
    print('3. View budget')
    print('4. Update budget')
    print('5. Exit')
    choice = input('Select an option: ')

    if choice == '1':
      amount = float(input('Enter an amount: '))
      category = input('Enter category: ')
      description = input('Enter description (optional): ')
      add_expense(data, amount, category, description=description)

    elif choice == '2':
      view_expenses(data)

    elif choice == '3':
      view_budget(data)

    elif choice == '4':
      category = input('Enter category to update: ')
      new_budget = float(input('Enter new budget: '))
      update_budget(data, category, new_budget)

    elif choice == '5':
      print('Exiting the application...')
      break

    else:
      print('Invalid option, please try again.')

if __name__ == '__main__':
  main()