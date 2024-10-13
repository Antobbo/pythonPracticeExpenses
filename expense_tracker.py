from expense import Expense
import csv
import pandas as pd

EMPTY_VALUE_ERROR_MESSAGE = "Value cannot be empty"
WRONG_TYPE_MESSAGE = "The value should be a number"
WRONG_EXPENSE_CATEGORY = f"Must be from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}"

def main():
    print(f"Expense app tracker.")
    user_input = getUserInput()
    new_expense = getExpense(user_input)
    print(f"data entered: {new_expense.name, new_expense.price, new_expense.category}")
    pushDataToFile(Expense.PATH_TO_FILE, new_expense)
    total_expenses = getTotalExpenditure()
    print(f"You've spent a total of £{total_expenses}")
    expenditure_by_category = getExpenditureBreakdown()

    for category, total in expenditure_by_category.items():
        category_name = Expense.EXPENSE_CATEGORY.get(category, 'Unknown')
        print(f'You spent £{total} for category {category_name}')

    remaining_allowance = getRamainingAllowance(total_expenses)
    print(f"You have left £")


def getUserInput():
    expense_name = input("Enter expense name: ")
    if not isinstance(expense_name, str) or expense_name.strip() == '':
        raise ValueError(EMPTY_VALUE_ERROR_MESSAGE);

    expense_cost = input("Enter how much you've spent (£): ")
    try:
        expense_cost = int(expense_cost)
    except ValueError:
        raise ValueError(WRONG_TYPE_MESSAGE) 
    
    print(f"Select a category: {Expense.EXPENSE_CATEGORY}")
    expense_category = input(f"Enter expense category from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}: ")
    try:
        expense_category = int(expense_category)    
        if expense_category < next(iter(Expense.EXPENSE_CATEGORY)) or expense_category > len(Expense.EXPENSE_CATEGORY):
            raise TypeError(WRONG_EXPENSE_CATEGORY);
    except ValueError:
        raise ValueError(WRONG_TYPE_MESSAGE)    
    return expense_name, float(expense_cost), int(expense_category)

def getExpense(user_input):
    return Expense(user_input[0], user_input[1], user_input[2])

def pushDataToFile(file_name, new_expense):
    expenseToAdd = [
            [new_expense.name, new_expense.price, new_expense.category]            
        ]
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenseToAdd)

def getTotalExpenditure():
    df = pd.read_csv(Expense.PATH_TO_FILE, header=None)
    #TODO: can we determine the column number somehow rather than hardcode it?
    return df[1].sum()

def  getExpenditureBreakdown():
    df = pd.read_csv(Expense.PATH_TO_FILE, header=None, names=['Expense', 'Price', 'Category'])
    return df.groupby('Category')['Price'].sum()

def getRamainingAllowance(total_expenses):
    return Expense.MONTHLY_BUDGET - total_expenses

if __name__ == "__main__":
    main()