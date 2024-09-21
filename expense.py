class Expense:
    MONTHLY_BUDGET = 2000;
    PATH_TO_FILE = "expenses.csv";
    EXPENSE_CATEGORY = {
     1: "food",
     2: "home",
     3: "work",
     4: "fun",
     5: "misc"   
    };

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        

    