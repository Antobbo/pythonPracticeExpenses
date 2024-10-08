import unittest
import expense
import expense_tracker
from unittest.mock import patch

class TestExpenseTracker(unittest.TestCase):

    #USER INPUT
    #given
    @patch('builtins.input', side_effect = ["coffee", 25, 1])
    def test_should_user_input_be_correct(self, mock_input):
        #when
        result = expense_tracker.getUserInput();
        #then
        self.assertEqual(result, ("coffee", 25, 1));
    
    #given 
    @patch('builtins.input', side_effect = ["", 25, 1])
    def test_should_throw_error_if_expense_name_empty(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            expense_tracker.getUserInput();
        #then
        self.assertIn(expense_tracker.EMPTY_VALUE_ERROR_MESSAGE, str(context.exception))

    #given
    @patch('builtins.input', side_effect = ["coffee", "dg", 1])
    def test_should_throw_error_if_expense_cost_not_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            expense_tracker.getUserInput();
        #then
        self.assertIn(expense_tracker.WRONG_TYPE_MESSAGE, str(context.exception))

    #given
    @patch('builtins.input', side_effect = ["coffee", "", 1])
    def test_should_throw_error_if_expense_cost_empty_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            expense_tracker.getUserInput();
        #then
        self.assertIn(expense_tracker.WRONG_TYPE_MESSAGE, str(context.exception))

    #given
    @patch('builtins.input', side_effect = ["coffee", 25, 6])
    def test_should_throw_error_if_expense_category_is_not_in_range(self, mock_input):
        with self.assertRaises(TypeError) as context:
            #when
            expense_tracker.getUserInput();
        #then
        self.assertIn(expense_tracker.WRONG_EXPENSE_CATEGORY, str(context.exception))

    #given
    @patch('builtins.input', side_effect = ["coffee", 25, 5])
    def test_should_input_all_be_correct(self, mock_input):
        #when
        result = expense_tracker.getUserInput();
        #then
        self.assertEqual(result, ("coffee", 25, 5));

    #given
    @patch('builtins.input', side_effect = ["coffee", 25, "5"])
    def test_should_input_all_be_correct_with_expense_category_as_string(self, mock_input):
        #when
        result = expense_tracker.getUserInput();
        #then
        self.assertEqual(result, ("coffee", 25, 5));

    #given
    @patch('builtins.input', side_effect = ["coffee", "10", "4"])
    def test_should_input_all_be_correct_with_expense_cost_as_string(self, mock_input):
        #when
        result = expense_tracker.getUserInput();
        #then
        self.assertEqual(result, ("coffee", 10, 4));

    #given
    @patch('builtins.input', side_effect = ["coffee", 25, "test"])
    def test_should_throw_error_when_expense_category_is_string(self, mock_input):
        with self.assertRaises(ValueError) as context:
            #when
            result = expense_tracker.getUserInput();
        #then
        self.assertIn(expense_tracker.WRONG_TYPE_MESSAGE, str(context.exception))

    #EXPENSE OBJECT
    def test_should_return_expese_object(self):
        #given
        user_input = ['burger', 10, 1]
        #when
        new_expense = expense_tracker.getExpense(user_input)
        #then
        self.assertIsInstance(new_expense, expense.Expense)
        self.assertEqual(new_expense.name, 'burger')
        self.assertEqual(new_expense.price, 10)
        self.assertEqual(new_expense.category, 1)

if __name__ == '__main__':
    unittest.main()

