import unittest
from say_the_number import say_the_number

class TestSayTheNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(say_the_number(0), "Zero.")

    def test_single_digit(self):
        self.assertEqual(say_the_number(5), "Five.")
        self.assertEqual(say_the_number(9), "Nine.")

    def test_double_digits(self):
        self.assertEqual(say_the_number(10), "Ten.")
        self.assertEqual(say_the_number(19), "Nineteen.")
        self.assertEqual(say_the_number(20), "Twenty.")
        self.assertEqual(say_the_number(21), "Twenty-one.")
        self.assertEqual(say_the_number(99), "Ninety-nine.")

    def test_triple_digits(self):
        self.assertEqual(say_the_number(100), "One hundred.")
        self.assertEqual(say_the_number(123), "One hundred and twenty-three.")
        self.assertEqual(say_the_number(900), "Nine hundred.")
        self.assertEqual(say_the_number(999), "Nine hundred and ninety-nine.")

    def test_thousands(self):
        self.assertEqual(say_the_number(1000), "One thousand.")
        self.assertEqual(say_the_number(2000), "Two thousand.")
        self.assertEqual(say_the_number(2010), "Two thousand and ten.")
        self.assertEqual(say_the_number(12345), "Twelve thousand, three hundred and forty-five.")
        self.assertEqual(say_the_number(999999), "Nine hundred and ninety-nine thousand, nine hundred and ninety-nine.")

    def test_millions(self):
        self.assertEqual(say_the_number(1000000), "One million.")
        self.assertEqual(say_the_number(1000001), "One million and one.")
        self.assertEqual(say_the_number(123456789), "One hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine.")
        self.assertEqual(say_the_number(999999999), "Nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine.")

    def test_billions(self):
        self.assertEqual(say_the_number(1000000000), "One billion.")
        self.assertEqual(say_the_number(2000000000), "Two billion.")
        self.assertEqual(say_the_number(2001000000), "Two billion and one million.")
        self.assertEqual(say_the_number(9876543210), "Nine billion, eight hundred and seventy-six million, five hundred and forty-three thousand, two hundred and ten.")

    def test_trillions(self):
        self.assertEqual(say_the_number(1000000000000), "One trillion.")
        self.assertEqual(say_the_number(2000000000000), "Two trillion.")
        self.assertEqual(say_the_number(2001000000000), "Two trillion and one billion.")
        self.assertEqual(say_the_number(999999999999999), "Nine hundred and ninety-nine trillion, nine hundred and ninety-nine billion, nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine.")
    
if __name__ == '__main__':
    unittest.main()
