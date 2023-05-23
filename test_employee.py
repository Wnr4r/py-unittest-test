from employee import Employee
import unittest

class TestEmpl(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Tomi', 'Sin', 6000)
        emp_2 = Employee('De', 'Borah', 6000)

        self.assertEqual(emp_1.email, 'Tomi.Sin@email.com')
        self.assertEqual(emp_2.email, 'De.Borah@email.com')


    def test_fullname(self):
        emp_1 = Employee('Tomi', 'Sin', 6000)
        emp_2 = Employee('De', 'Borah', 6000)

        self.assertEqual(emp_1.fullname, 'Tomi Sin')
        self.assertEqual(emp_2.fullname, 'De Borah')







if __name__ == '__main__':
    unittest.main()
