import unittest
import expense
import expense_tracker
from unittest.mock import patch
import os
import pandas as pd

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

    #FILE HANDLING
    def test_should_create_file(self):
        #given
        file_name = expense.Expense.PATH_TO_FILE;
        user_input = ['burger', 15, 1]
        new_expense = expense_tracker.getExpense(user_input)
        #when
        expense_tracker.pushDataToFile(file_name, new_expense)
        #then
        self.assertTrue(os.path.isfile(file_name))
        self.delete_file(file_name)        

   
    def test_should_file_created_and_updated_have_right_number_of_rows_and_right_values(self):
        #given
        file_name = expense.Expense.PATH_TO_FILE;
        user_input = ['burger', 10, 1]
        user_input_2 = ['electricity', 100, 2]
        new_expense = expense_tracker.getExpense(user_input)
        new_expense_2 = expense_tracker.getExpense(user_input_2)
        expense_tracker.pushDataToFile(file_name, new_expense)
        expense_tracker.pushDataToFile(file_name, new_expense_2)
        df = pd.read_csv(file_name, header=None)
        rows = len(df)
        self.assertEqual(rows, 2, "Row number should be 2")
        col_list = df[0].tolist()
        self.assertTrue('burger' in col_list)
        self.assertTrue('electricity' in col_list)
        self.delete_file(file_name)

    def test_should_get_total_expenditure(self):
        #given        
        file_name = expense.Expense.PATH_TO_FILE;
        user_input = ['burger', 10, 1]
        user_input_2 = ['electricity', 100, 2]
        user_input_3 = ['water', 300, 2]
        user_input_4 = ['gas', 500, 2]
        expected_total = 910
        new_expense = expense_tracker.getExpense(user_input)
        new_expense_2 = expense_tracker.getExpense(user_input_2)
        new_expense_3 = expense_tracker.getExpense(user_input_3)
        new_expense_4 = expense_tracker.getExpense(user_input_4)
        expense_tracker.pushDataToFile(file_name, new_expense)
        expense_tracker.pushDataToFile(file_name, new_expense_2)
        expense_tracker.pushDataToFile(file_name, new_expense_3)
        expense_tracker.pushDataToFile(file_name, new_expense_4)
        #when
        actual_total = expense_tracker.getTotalExpenditure()
        #then
        self.assertEqual(expected_total, actual_total, "They should be equal")
        self.delete_file(file_name)


    def test_should_get_expenditure_breakdown(self):
        #given        
        file_name = expense.Expense.PATH_TO_FILE;
        user_input = ['burger', 10, 1]
        user_input_2 = ['electricity', 100, 2]
        user_input_3 = ['water', 300, 2]
        user_input_4 = ['gas', 500, 2]
        expected_result = {1: 10, 2: 900}
        new_expense = expense_tracker.getExpense(user_input)
        new_expense_2 = expense_tracker.getExpense(user_input_2)
        new_expense_3 = expense_tracker.getExpense(user_input_3)
        new_expense_4 = expense_tracker.getExpense(user_input_4)
        expense_tracker.pushDataToFile(file_name, new_expense)
        expense_tracker.pushDataToFile(file_name, new_expense_2)
        expense_tracker.pushDataToFile(file_name, new_expense_3)
        expense_tracker.pushDataToFile(file_name, new_expense_4)
        #when
        actual_result = expense_tracker.getExpenditureBreakdown()
        #then
        self.assertEqual(expected_result, actual_result.to_dict(), "They should be equal")
        self.delete_file(file_name)

    def test_should_calculate_remaining_allowance(self):
        expected_remaining_allowance = 1400
        actual_remaining_allowance = expense_tracker.getRamainingAllowance(600)        
        self.assertEqual(expected_remaining_allowance, actual_remaining_allowance, "They should be equal")
        

    def delete_file(self, file_name):
        # Clean up by removing the file after the test
        if os.path.isfile(file_name):
            os.remove(file_name)

if __name__ == '__main__':
    unittest.main()

