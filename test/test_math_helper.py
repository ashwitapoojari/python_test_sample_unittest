from python_test_sample.math_helper import MathHelper
from unittest import TestCase
from unittest.mock import patch


class TestMathHelper(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.math_helper = MathHelper()

    def test_add_result(self):
        """
        It should return the result of operation (addition)
        """

        self.assertEqual(self.math_helper.calc('addition', 1, 1), 2)

    @patch('python_test_sample.math_helper.MathHelper._add')
    def test_add_called(self, mocked_add):
        """
        It should call the method "_add" when "calc" is called with "addition"
        """

        self.math_helper.calc('addition', 1, 1)

        self.assertTrue(mocked_add.called)

    def test_sub_result(self):
        """
        It should return the result of operation (subtraction)
        """

        self.assertEqual(self.math_helper.calc('subtraction', 2, 1), 1)

    @patch('python_test_sample.math_helper.MathHelper._sub')
    def test_sub_called(self, mocked_sub):
        """
        It should call the method "_sub" when "calc" is called with "subtraction"
        """

        self.math_helper.calc('subtraction', 2, 1)

        self.assertTrue(mocked_sub.called)

    def test_mul_result(self):
        """
        It should return the result of operation (multiplication)
        """

        self.assertEqual(self.math_helper.calc('multiplication', 2, 1), 2)

    @patch('python_test_sample.math_helper.MathHelper._mul')
    def test_mul_called(self, mocked_mul):
        """
        It should call the method "_mul" when "calc" is called with "multiplication"
        """

        self.math_helper.calc('multiplication', 2, 1)

        self.assertTrue(mocked_mul.called)

    def test_div_result(self):
        """
        It should return the result of operation (division)
        """

        self.assertEqual(self.math_helper.calc('division', 4, 2), 2)

    @patch('python_test_sample.math_helper.MathHelper._div')
    def test_div_called(self, mocked_div):
        """
        It should call the method "_div" when "calc" is called with "division"
        """

        self.math_helper.calc('division', 4, 2)

        self.assertTrue(mocked_div.called)

    def test_incorrect_operation(self):
        """
        It should return "None" if the first parameter is incorrect
        """

        self.assertEqual(self.math_helper.calc('incorrect', 1, 1), None)
