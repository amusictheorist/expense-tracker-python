# Simple Expense Tracker and Budget Planner

A command-line application that helps track your expenses, manage your budget, and generate monthly reports.

## Features
- Add, view, and delete expenses
- Set and update budgets for different categories (e.g., Food, Entertainment)
- Generate a monthly expense report
- Tracks expenses in categories and calculates remaininf budget

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/expense-tracker.git
```
2. **Navigate to the project directory:**
```bash
cd expense-tracker
```
3. **Install dependencies (if any):**
If you're using a virtual environment, you might want to install dependencies like `datetime`. (For now this is a simple script without any additional libraries).

4. **Run the application:**
```bash
python main.py
```
## Usage
Once the application is running, you can interact with the following options:
1. **Add expense:** add a new expense, specifying the amount, category, and descrpition (optional).
2. **View expenses:** view all recorded expenses.
3. **View budget:** see the budget breakdown for all categories.
4. **Update budget:** modify the budget for a specific category.
5. **Delete expense:** remove an expense from the records.
6. **Monthly report:** generate a report for the current month showing total expenses, category-wise spending, and remaining budget.
7. **Exit:** exit the application.

### Example output
```bash
--- Expense Tracker CLI ---
1. Add expense
2. View expenses
3. View budget
4. Update budget
5. Delete expense
6. Monthly report
7. Exit
Select an option: 1
Enter an amount: 50
Enter category: food
Enter description (optional): Lunch
Expense of 50.0 added in category 'food'.
```
### Example monthly report
```bash
Monthly report:
Total expenses: 200
Category-wise spending:
  Food          : Spent 100 , Budget 300 , Remaining 200 
  Entertainment : Spent 100 , Budget 150 , Remaining 50  

--------------------------------------------------
Total          : Spent 200 , Budget 450 , Remaining 250
```
## Contributing
1. Fork the repository
2. Create a new branch (`git chekout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

This project is for personal use only and is not licensed for distribution.