import unittest
import expense

class TestExpense(unittest.TestCase):
    def test_should_expense_class_exist(self):
        # check if the expense class exists, might not strictly need this test though
        self.assertTrue(hasattr(expense, "Expense"))

    def test_should_categories_have_expected_elements(self):
        self.assertIn("food", expense.Expense.EXPENSE_CATEGORY[1]);
        self.assertIn("home", expense.Expense.EXPENSE_CATEGORY[2]);
        self.assertIn("work", expense.Expense.EXPENSE_CATEGORY[3]);
        self.assertIn("fun", expense.Expense.EXPENSE_CATEGORY[4]);
        self.assertIn("misc", expense.Expense.EXPENSE_CATEGORY[5]);
        self.assertNotIn("Random", expense.Expense.EXPENSE_CATEGORY[1]);        

    def test_should_length_expenses_category_be_as_expected(self):
        self.assertEqual(len(expense.Expense.EXPENSE_CATEGORY), 5);

    def test_should_variable_have_right_values(self):
        #given
        name = "Coffee"
        category = "Food"
        price = 3.50

        #when
        current_expense = expense.Expense(name, price, category);

        #then
        self.assertEqual(current_expense.category, category);
        self.assertEqual(current_expense.name, name);
        self.assertEqual(current_expense.price, price);

if __name__ == '__main__':
    unittest.main()