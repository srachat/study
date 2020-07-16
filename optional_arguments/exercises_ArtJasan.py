from typing import Optional, List


# Exercises plan:
# 1) Passing arguments into a function
# 2) Fix the function so it would work correctly
# 3) Write your own function for handling different cases
# OPTIONAL: 4) Fix the function with optional argument which takes a list


# 1) Passing arguments into a function
def greet_a_person(
		name: str,
		greeting: str = "Have a good day!",
		amount_of_repeats: int = 1
) -> str:
	"""
	Here a person should be greeted by a standard phrase 1 time
	>>> greet_a_person("Pavel")
	'Pavel, Have a good day!'

	In the same manner as the above example, write another tests:

	Here a person should be greeted by another phrase 1 time
	# FIXME
	>>> greet_a_person("Pavel", greeting="Nice to see you!")
	'Pavel, Nice to see you!'

	Here a person should be greeted be a standard phrase 3 times
	# FIXME
	>>> greet_a_person(name="Pavel", amount_of_repeats=3)
	'Pavel, Have a good day! Pavel, Have a good day! Pavel, Have a good day!'

	Here a person should be greeted by another phrase 3 times
	# FIXME
	>>> greet_a_person(name="Pavel",greeting="Nice to see you!", amount_of_repeats=3)
	'Pavel, Nice to see you! Pavel, Nice to see you! Pavel, Nice to see you!'

	>>> greet_a_person(greeting="Nice to see you!", amount_of_repeats=-1)
	Traceback (most recent call last):
	...
	TypeError: greet_a_person() missing 1 required positional argument: 'name'

	Function to greet a person with some phrase.
	:param name: this is a required argument. name of a person to greet
	:param greeting: this is an optional argument. pass a phrase if you want to greet a person with it
	:param amount_of_repeats: this is an optional argument. indicates the amount of times to repeat the greeting
	:return: string of greeting
	"""
	return ' '.join([f"{name}, {greeting}" for _ in range(amount_of_repeats)])


# Questions:
# - what would happen if a user would skip the `name` argument?
# - what would happen if a user would provide a negative value for `amount_of_repeats`? or a string instead of integer?

# Answers:
# - User will get a error: greet_a_person() missing 1 required positional argument: 'name'
# - User will get a Nothing (if a user uses a negative value)
# - User will get a error: 'str' object cannot be interpreted as an integer (if a user uses a string), because we
# specified this argument like a integer.
# ----------------------------------------------------------------


# 2) Fix the function so it would correctly process given examples:
def create_a_car(
		model: str,
		engine: str,
		amount_of_doors: int,
		display_diagonal: Optional[int]
) -> str:
	"""
	Following tests should pass:

	>>> create_a_car(model="audi",engine="v6",amount_of_doors=5, display_diagonal=None)
	'configuration of audi: engine v6, amount of doors: 5'

	>>> create_a_car(model="volkswagen",engine="v4", amount_of_doors=4, display_diagonal=None)
	'configuration of volkswagen: engine v4, amount of doors: 4'

	>>> create_a_car(model="mercedes",engine='v4', amount_of_doors=5, display_diagonal=None)
	'configuration of mercedes: engine v4, amount of doors: 5'

	>>> create_a_car(model="opel",engine='v4', amount_of_doors=4, display_diagonal=None)
	'configuration of opel: engine v4, amount of doors: 4'

	>>> create_a_car(model="porsche",engine="v8",amount_of_doors=4, display_diagonal=20)
	'configuration of porsche: engine v8, amount of doors: 4, display diagonal: 20 inches'

	>>> create_a_car(engine="v8",amount_of_doors=4, display_diagonal=20)
	Traceback (most recent call last):
	...
	TypeError: create_a_car() missing 1 required positional argument: 'model'

	This function creates a car with given model name, engine and amount of doors.
	:param model: string indicating a name of a model
	:param engine: string indicating which type of motor is used
	:param amount_of_doors: self descriptive
	:param display_diagonal: size of a display in inches
	:return: string with car configuration
	"""
	configuration_string = f"configuration of {model}: engine {engine}, amount of doors: {amount_of_doors}"
	if display_diagonal is not None:
		configuration_string += f", display diagonal: {display_diagonal} inches"
	return configuration_string


# ----------------------------------------------------------------


# 3) Write a function with typing hints which would construct a string of a person profile
# Change `args` to some real parameters
def create_person_profile(
		name: str,
		age: int,
		hobby: Optional[str],
		city: Optional[str] = 'New York',

) -> str:
	"""
	>>> create_person_profile("Vova", 24,city="Prague", hobby="Warhammer 40k")
	'Person Vova is 24 years old, lives in Prague, and loves Warhammer 40k'

	>>> create_person_profile("Dave", 32, hobby=None)
	'Person Dave is 32 years old, lives in New York'

	>>> create_person_profile("Bob", 27, hobby="weed")
	'Person Bob is 27 years old, lives in New York, and loves weed'

	>>> create_person_profile("Bröther", 18, city="Amsterdam", hobby=None)
	'Person Bröther is 18 years old, lives in Amsterdam'

	>>> create_person_profile(age=18, city="Amsterdam", hobby=None)
	Traceback (most recent call last):
	...
	TypeError: create_person_profile() missing 1 required positional argument: 'name'

	:param name: string name of a person. required
	:param age: int age of a person. required
	:param city: string city of a person. optional. default - "Prague"
	:param hobby: string hobby of a person. optional. no default
	:return: string of a person profile
	"""
	info = f"Person {name} is {age} years old"
	if city is not None:
		info += f", lives in {city}"
	if hobby is not None:
		info += f", and loves {hobby}"
	return info


# ----------------------------------------------------------------


# Following exercise is optional, since it has higher level of difficulty
# 4) Fix the function with optional argument which takes a list
# 		Uncomment the function to start fixing it
# See the comment after the function if you are stuck with the solution

# noinspection PyDefaultArgument
def append_to_list(
		person_to_append: str,
		list_of_persons: List[str] = None
) -> List[str]:
	"""
	Append the given person to a list of already existing persons.
	If no list of persons provided, append to a new list.

	>>> append_to_list("Vova", ["Pavel", "Artem", "Ravil"])
	['Pavel', 'Artem', 'Ravil', 'Vova']

	>>> append_to_list("Artem")
	['Artem']

	# FIXME: this will fail! outputs ['Artem', 'Vova'] instead of ['Vova']
	>>> append_to_list("Vova")
	['Vova']

	:param person_to_append: string name of a person to append
	:param list_of_persons: list of strings of persons
	:return: list of strings of persons
	"""
	if list_of_persons is None:
		list_of_persons = []
	list_of_persons.append(person_to_append)
	return list_of_persons


# Uncomment following code to inspect the problem

append_to_list("Vova", ["Pavel", "Artem", "Ravil"])
print(append_to_list.__defaults__)  # should output []
append_to_list("Artem")
print(append_to_list.__defaults__)  # should output []
append_to_list("Vova")
print(append_to_list.__defaults__)  # should output []

# Articles which would help to solve the issue:
# - https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
# - https://docs.python-guide.org/writing/gotchas/


if __name__ == "__main__":
	import doctest
	doctest.testmod()
