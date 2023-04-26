
# `say_the_number` function

This Python function takes an integer and returns its word representation using the `inflect` library.

## Installation

To use the `say_the_number` function, you'll need to install the `inflect` library:

```
pip install inflect
```

## Usage

Here's an example of how to use the `say_the_number` function:

```python
from say_the_number import say_the_number

result = say_the_number(42)
print(result)  # prints "forty-two."
```

The `say_the_number` function takes an integer as its argument and returns its word representation as a string with a period at the end.

For example, `say_the_number(123)` returns the string `"one hundred and twenty-three."`.

Note that the function currently only supports integers between 0 and 999,999.

## Testing

This implementation includes unit tests for the `say_the_number` function using the `unittest` module in Python.

To run the tests, save the code in a file called `test_say_the_number.py` and run the following command:

```
python -m unittest test_say_the_number.py
```



This code defines the `TestSayTheNumber` test case class, which contains a `test_say_the_number` method that defines several test cases using the `assertEqual` method to check that the `say_the_number` function returns the expected results for various input values.

When you run the `test_say_the_number.py` script, `unittest.main()` will run the `TestSayTheNumber` test case class and report the results.

## Contribution

If you find any issues or bugs in this implementation, or if you have any suggestions for improvement, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/say_the_number). 

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).