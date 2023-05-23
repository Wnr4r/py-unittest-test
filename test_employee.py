from employee import Employee
import unittest

class TestEmpl(unittest.TestCase):

    def setUp(self) -> None:
        print("Setup")
        self.emp_1 = Employee('Tomi', 'Sin', 6000)
        self.emp_2 = Employee('De', 'Borah', 6000)

    def tearDown(self) -> None:
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





if __name__ == '__main__':
    unittest.main()
