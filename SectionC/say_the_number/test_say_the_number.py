import unittest
import inflect
from say_the_number import say_the_number

class TestSayTheNumber(unittest.TestCase):
    def test_say_the_number(self):
        self.assertEqual(say_the_number(0), 'Zero.')
        self.assertEqual(say_the_number(1), 'One.')
        self.assertEqual(say_the_number(9), 'Nine.')
        self.assertEqual(say_the_number(10), 'Ten.')
        self.assertEqual(say_the_number(11), 'Eleven.')
        self.assertEqual(say_the_number(19), 'Nineteen.')
        self.assertEqual(say_the_number(20), 'Twenty.')
        self.assertEqual(say_the_number(21), 'Twenty-one.')
        self.assertEqual(say_the_number(99), 'Ninety-nine.')
        self.assertEqual(say_the_number(100), 'One hundred.')
        self.assertEqual(say_the_number(101), 'One hundred and one.')
        self.assertEqual(say_the_number(999), 'Nine hundred and ninety-nine.')
        self.assertEqual(say_the_number(1000), 'One thousand.')
        self.assertEqual(say_the_number(1001), 'One thousand and one.')
        self.assertEqual(say_the_number(123456), 'One hundred and twenty-three thousand, four hundred and fifty-six.')

if __name__ == '__main__':
    unittest.main()