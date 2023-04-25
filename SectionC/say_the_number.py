def say_the_number(num):
    """
    Returns a string that spells out the given number in words.

    Args:
        num (int): The number to spell out.

    Returns:
        str: A string that spells out the given number in words.
    """
    # Define lists of words for the ones digits, tens digits, and suffixes for larger numbers.
    ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    suffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion"]

    # If the number is less than 20, return the corresponding word from the ones list.
    if num < 20:
        return ones[num] + "."

    # Convert the number to a string and split it into a list of digits.
    numStr = str(num)
    numArr = [int(d) for d in numStr]

    # If the number has two digits, combine the words for the tens and ones digits.
    if len(numArr) == 2:
        result =  tens[numArr[0]] + ("-" + ones[numArr[1]] if numArr[1] != 0 else "") + "."
        return result[0]+result[1:].lower()

    # If the number has more than two digits, split it into groups of three and spell out each group with a corresponding suffix.
    words = []
    suffixIndex = 0

    while len(numArr) > 0:
        threeDigits = numArr[-3:]
        threeDigitsStr = "".join(map(str, threeDigits)).zfill(3)

        if threeDigitsStr != "000":
            hundredsDigit = int(threeDigitsStr[0])
            tensDigit = int(threeDigitsStr[1])
            onesDigit = int(threeDigitsStr[2])

            # Combine the words for the hundreds, tens, and ones digits, and add the corresponding suffix.
            hundredsWord = ones[hundredsDigit] + " hundred" if hundredsDigit != 0 else ""
            tensWord = tens[tensDigit] if tensDigit != 0 else ""
            onesWord = ones[tensDigit*10 + onesDigit] if tensDigit == 1 else ones[onesDigit]

            threeDigitsWords = " ".join(filter(bool, [hundredsWord, tensWord, onesWord]))
            suffix = suffixes[suffixIndex] if suffixIndex != 0 else ""

            words.insert(0, threeDigitsWords + " " + suffix)

        numArr = numArr[:-3]
        suffixIndex += 1
    
    # Combine the words for each group of three digits with commas, and return the final result.
    result = ", ".join(words) + "."
    return result[0]+result[1:].lower()




import unittest

class TestSayTheNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(say_the_number(0), "Zero.")

    def test_single_digit(self):
        self.assertEqual(say_the_number(5), "Five.")
        self.assertEqual(say_the_number(9), "Nine.")

    def test_teens(self):
        self.assertEqual(say_the_number(11), "Eleven.")
        self.assertEqual(say_the_number(19), "Nineteen.")

    def test_tens(self):
        self.assertEqual(say_the_number(20), "Twenty.")
        self.assertEqual(say_the_number(45), "Forty-five.")
        self.assertEqual(say_the_number(99), "Ninety-nine.")

    def test_hundreds(self):
        self.assertEqual(say_the_number(100), "One hundred.")
        self.assertEqual(say_the_number(345), "Three hundred forty-five.")
        self.assertEqual(say_the_number(999), "Nine hundred ninety-nine.")

    def test_thousands(self):
        self.assertEqual(say_the_number(1000), "One thousand.")
        self.assertEqual(say_the_number(3456), "Three thousand, four hundred fifty six .")
        self.assertEqual(say_the_number(999999), "Nine hundred ninety nine thousand, nine hundred ninety nine .")

    def test_millions(self):
        self.assertEqual(say_the_number(1000000), "One million.")
        self.assertEqual(say_the_number(1234567), "One million, two hundred thirty four thousand, five hundred sixty seven .")
        self.assertEqual(say_the_number(999999999), "Nine hundred ninety nine million, nine hundred ninety nine thousand, nine hundred ninety nine .")

    def test_large_numbers(self):
        self.assertEqual(say_the_number(1000000000), "One billion.")
if __name__ == '__main__':
    unittest.main()
