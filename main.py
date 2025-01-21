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

def validate_input(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print('Inva;id input, Please enter a valid number.')

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

def delete_expense(data):
  if not data['expenses']:
    print('No expenses to delete.')
    return
  
  print('\nExpenses:')
  for idx, exp in enumerate(data['expenses']):
    print(f"{idx}: {exp['date']} | {exp['category']} | {exp['amount']} {exp['description']}")

  index = int(input('\nEnter the index of the expense to delete: '))
  if 0 <= index < len(data['expenses']):
    deleted = data['expenses'].pop(index)
    save_data(data)
    print(f'Deleted expense: {deleted}')
  else:
    print('Invalid index.')

def generate_monthly_report(data):
  current_month = datetime.now().strftime('%Y-%m')
  monthly_expenses = [exp for exp in data['expenses'] if exp['date'].startswith(current_month)]

  print('\nMonthly report:')
  print(f"Total expenses: {sum(exp['amount'] for exp in monthly_expenses)}")
  print('Category-wise spending:')
  for category, budget in data['budgets'].item():
    spent = sum(exp['amount'] for exp in monthly_expenses if exp['category'] == category)
    print(f'  {category.capitalize()}: Spent {spent}, Budget {budget}, Remaining {budget - spent}')

def main():
  data = load_data()

  while True:
    print('\n--- Expense Tracker CLI ---')
    print('1. Add expense')
    print('2. View expenses')
    print('3. View budget')
    print('4. Update budget')
    print('5. Delete expense')
    print('6. Monthly report')
    print('7. Exit')
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
      delete_expense(data)

    elif choice == '6':
      generate_monthly_report(data)

    elif choice == '7':
      print('Exiting the application...')
      break

    else:
      print('Invalid option, please try again.')

if __name__ == '__main__':
  main()