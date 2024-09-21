from expense import Expense
EMPTY_VALUE_ERROR_MESSAGE = "Value cannot be empty"
WRONG_TYPE_MESSAGE = "The value should be a number"
WRONG_EXPENSE_CATEGORY = f"Must be from {next(iter(Expense.EXPENSE_CATEGORY))} to {len(Expense.EXPENSE_CATEGORY)}"

def main():
    print(f"Expense app tracker.")
    user_input = getUserInput()
    new_expense = getExpense(user_input)
    print(f"data entered: {new_expense.name, new_expense.price, new_expense.category}")

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

if __name__ == "__main__":
    main()