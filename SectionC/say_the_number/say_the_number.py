import inflect

def say_the_number(number: int) -> str:

    """
    Convert an integer to its word representation using the inflect library.

    Args:
        number (int): The number to be converted to words.

    Returns:
        str: The word representation of the given number, with a dot at the end.
    """
    number_to_word = inflect.engine()
    return number_to_word.number_to_words(number).capitalize() + '.'