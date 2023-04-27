
  
# Define dictionaries for representing digits
ones = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}



def say_the_number(n):
    """
    Convert an integer into its English-language representation.

    Args:
        n: An integer.

    Returns:
        A string representing the input integer in English.

    Examples:
        >>> say_the_number(123456789)
        'One hundred twenty-three million, four hundred fifty-six thousand, seven hundred eighty-nine.'
        >>> say_the_number(0)
        'Zero.'
    """

    # Special case for zero
    if 99<n<1000 and n%100==0:
        return (ones[n//100] + " hundred.").capitalize()
    if n==0:
        return "Zero."
    pieces,sorted_rank = get_number_pieces(n)
    return join_with_commas(pieces,sorted_rank).capitalize() +"."
    

def get_number_pieces(number):
    """ getting the number pieces
	
	Args:
		n: An integer.
	
	Returns:
		A list of strings representing the input integer in English.
		
	Examples:
		>>> get_number_pieces(123456789)
		['one hundred twenty-three million', 'four hundred fifty-six thousand', 'seven hundred eighty-nine']"""
    

    # Split the number into groups of `five` digits
    numbers_rank = ["", " thousand", " million", " billion", " trillion"]
    sorted_rank = [(number//(10**(3*i)))%1000 for i in range(5)]
    return [say_smaller(sorted_rank[i]) + numbers_rank[i] for i in range(5) if sorted_rank[i]!=0], sorted_rank


def say_smaller(n):
	"""
	Convert a number up to 999 trillion into its English-language representation.

	Args:
		n: An integer up to 999 trillion.

	Returns:
		A string representing the input integer in English.

	Examples:
		>>> say_smaller(123456789)
		'one hundred twenty-three million, four hundred fifty-six thousand, seven hundred eighty-nine'
	"""
	# Convert the hundreds digit to English and append "hundred" if non-zero
	if n//100:
		result = ones[n//100] + " hundred"
	else:
		result = ""

	# If there are both hundreds and tens/ones digits, insert an "and"
	if n//100 and n%100:
		result += " and "

	# Convert the tens and ones digits to English and append to the result
	result += say_small(n%100)

	return result

def say_small(n):
	"""
	Convert a number between 1 and 999 into its English-language representation.

	Args:
		n: An integer between 1 and 999.

	Returns:
		A string representing the input integer in English.

	Examples:
		>>> say_small(123)
		'one hundred twenty-three'
	"""
	if n>=20: 
		# For numbers greater than or equal to 20, use the tens dictionary and append the ones digit if it is non-zero
		return tens[n//10] + "-"*bool(n%10) + ones[n%10]*bool(n%10)
	if n>=10: 
		# For numbers between 10 and 19, use the teens dictionary
		return teens[n]
	return ones[n] # For single-digit numbers, use the ones dictionary


def join_with_commas(pieces, sorted_rank):
	"""
	Join a list of strings with commas.

	Args:
		pieces: A list of strings.

	Returns:
		A string consisting of the input strings joined with commas.

	Examples:
		>>> join_with_commas(["one", "two", "three"])
		'one, two, three'
	"""
	return ", ".join(pieces[1:][::-1]) + " and " + pieces[0] if len(pieces)>1 and sorted_rank[0]<100 else ", ".join(pieces[::-1]) if len(pieces)>1 else pieces[0]


