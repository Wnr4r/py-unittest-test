from employee import Employee
import unittest
from unittest.mock import patch

class TestEmpl(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        """runs at the beginning of each test method"""
        print("Setup")
        self.emp_1 = Employee('Tomi', 'Sin', 6000)
        self.emp_2 = Employee('De', 'Borah', 6000)

    def tearDown(self) -> None:
        """runs at the end of each test method"""
        print("tearDown\n")

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Tomi.Sin@email.com')
        self.assertEqual(self.emp_2.email, 'De.Borah@email.com')


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Tomi Sin')
        self.assertEqual(self.emp_2.fullname, 'De Borah')


    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 6300)
        self.assertEqual(self.emp_2.pay, 6300)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule("June")
            mocked_get.assert_called_with('http://company.com/Tomi/June')  # ensure it's called with the right url
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("May")
            mocked_get.assert_called_with('http://company.com/De/May')  # ensure it's called with the right url
            self.assertEqual(schedule, 'Bad Response!')






if __name__ == '__main__':
    unittest.main()
