import doctest
from operator import add
from typing import Any, Callable
import unittest
from unittest import TestCase

# Couple of useful links for refreshing your knowledge
# - https://realpython.com/python-lambda/
# - https://realpython.com/lessons/what-is-lambda-function/
# - https://www.programiz.com/python-programming/anonymous-function
# - https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

# Exercises plan
# 1) Quick refresher: create couple of simple lambda functions
# 2) Usage in standard different higher order functions


# Do not assign the lambda function to a variable
# If you need to save a function to any variable, use `def` instead, which has more clear syntax
# If you use PyCharm or any other intelligent IDE
# notice that the comment under the assigned variable
this_is_wrong = lambda do_not_assign_lambda_to_variable: do_not_assign_lambda_to_variable


# Use such approach instead
def this_is_correct():
	pass


# As you can see, both are functions
# Uncomment to execute:
# print(type(this_is_wrong))
# print(type(this_is_correct))


# 1) Quick refresher: create couple of simple lambda functions

# --------> READ THE FUNCTION DOCS! <--------

# Imagine having following function:
def apply_function_to_args(some_function: Callable, *args: Any) -> Any:
	"""
	This function takes some first order function as the first parameter.
	This function is applied to the arguments passed after the function.
	Result of the function run is returned.
	:param some_function: Callable, some first-order function
	:param args: Any, arguments which should be passed to first order function
	:return: Any, result from the first order function

	Lambda can have single argument:
	>>> apply_function_to_args(lambda string: string.upper(), 'python')
	'PYTHON'

	Lambda can also be passed with several arguments:
	>>> apply_function_to_args(lambda x, y: x + y, 1, 2)
	3

	Another ways to write the previous example:
	>>> apply_function_to_args(sum, (2, 3))
	5
	>>> apply_function_to_args(add, 3, 5)
	8

	TODO: Write correct lambda functions

	FIXME:
	>>> apply_function_to_args(..., )

	FIXME:
	>>> apply_function_to_args(..., 'PYTHON')
	'python'

	FIXME:
	>>> apply_function_to_args(..., [1, 2, 3, 4, 5])
	[2, 3, 4]

	FIXME:
	>>> apply_function_to_args(..., 10, range(20))
	True

	FIXME:
	>>> apply_function_to_args(..., 1, 100)
	100
	"""
	return some_function(*args)


# 2) Usage in standard different higher order functions
class LambdaTestCase(TestCase):
	"""
	This class os fpr testing lambda functions in different higher order functions such as:
	- map()
	- filter()
	- sorted()

	This is another way to test correctness of written code: using unittest
		- All tests should be placed into the class, which is subclassed from unittest.TestCase
		- Each test name should start with the prefix `test_`
		- If there is any presets which should be made before each test run, overwrite the function `setUp`

	It is not a very good practice to mix unittests with normal code, but we we'll close our eyes on that for
	studying purposes :)
	"""
	def setUp(self) -> None:
		# You can make any presets if you need
		pass

	# Get information about `map()` function:
	# - https://www.geeksforgeeks.org/python-map-function/
	# - https://www.programiz.com/python-programming/methods/built-in/map

	def test_map_example(self):
		mapped = list(map(
			lambda number: number.upper(),
			["one", "two", "three", "four", "five"]
		))
		self.assertListEqual(mapped, ["ONE", "TWO", "THREE", "FOUR", "FIVE"])

	def test_map_example_another_approach(self):
		list_of_numbers = ["one", "two", "three", "four", "five"]
		mapped = [number.upper() for number in list_of_numbers]
		self.assertListEqual(mapped, ["ONE", "TWO", "THREE", "FOUR", "FIVE"])

	# FIXME
	def test_map_string_addition(self):
		mapped = list(map(..., ["first", "second", "third"]))
		self.assertListEqual(mapped, ["first argument", "second argument", "third argument"])

	# FIXME
	def test_map_extract_x_coordinate(self):
		points = [(0, 0), (12, 15), (1, -1), (-10.5, -10)]
		mapped = list(map(..., points))
		self.assertListEqual(mapped, [0, 12, 1, -10.5])

	# FIXME
	def test_map_multiple_lists(self):
		mapped = list(map(
			...,
			["first", "second", "third"],
			["SENTENCE", "ARGUMENT", "PHRASE"]
		))
		self.assertListEqual(
			mapped,
			["FIRST sentence", "SECOND argument", "THIRD phrase"]
		)

	# Get information about `filter() function:
	# - https://www.geeksforgeeks.org/filter-in-python/
	# - https://kite.com/python/answers/how-to-filter-a-list-in-python

	def test_filter_example_less_than_five(self):
		list_of_numbers = [1, 10, 12, 4, 5, 5.5, 4.5]
		filtered = list(filter(lambda number: number < 5, list_of_numbers))
		self.assertListEqual(filtered, [1, 4, 4.5])

	# FIXME
	def test_filter_is_numeric(self):
		list_of_strings = ["one", "another", "123", "12.5", "-15", "0"]
		filtered = list(filter(..., list_of_strings))
		self.assertListEqual(filtered, ["one", "another"])

	# FIXME
	def test_filter_first_symbol_upper(self):
		list_of_strings = ["one", "Another", "123", "Last"]
		filtered = list(filter(..., list_of_strings))
		self.assertListEqual(filtered, ["Another", "Last"])

	# FIXME
	def test_filter_not_none(self):
		list_of_elements = [None, 2, None, "four", 12.5, None]
		filtered = list(filter(..., list_of_elements))
		self.assertListEqual(filtered, [2, "four", 12.5])

	# Get information about `sorted() function:
	# - https://docs.python.org/3/howto/sorting.html
	# - https://realpython.com/python-sort/

	def test_sorted_integers_without_key(self):
		list_of_numbers = [1, 10, -1, 2, -3, 4]
		sorted_numbers = sorted(list_of_numbers)
		self.assertListEqual(sorted_numbers, [-3, -1, 1, 2, 4, 10])

	def test_sorted_integers_with_key(self):
		list_of_numbers = [1, 10, -1, 2, -3, 4]
		sorted_numbers = sorted(list_of_numbers, key=lambda number: -number)
		self.assertListEqual(sorted_numbers, [10, 4, 2, 1, -1, -3])

	# FIXME
	def test_sorted_strings_first_symbol(self):
		list_of_names = ["Pavel", "Vova", "Artem", "Ravil"]
		sorted_names = sorted(list_of_names, key=...)
		self.assertListEqual(sorted_names, ["Artem", "Pavel", "Ravil", "Vova"])

	# FIXME
	def test_sorted_strings_last_symbol(self):
		list_of_names = ["Ravil", "Vova", "Artem", "Pavel"]
		sorted_names = sorted(list_of_names, key=...)
		# Why is "Ravil" before "Pavel"?
		self.assertListEqual(sorted_names, ["Vova", "Ravil", "Pavel", "Artem"])

	# FIXME
	def test_sorted_points(self):
		points = [(0, 0), (12, 15), (1, -1), (-10.5, -10)]
		sorted_points = sorted(points, key=...)
		self.assertListEqual(sorted_points, [(-10.5, -10), (0, 0), (1, -1), (12, 15)])


if __name__ == '__main__':
	doctest.testmod()
	unittest.main()
