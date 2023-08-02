"""Memoization is the practice of storing intermediate results of an
algorithm so that repeated values can be fetched from memory rather than
calculated with system resources (time and energy).

(https://www.geeksforgeeks.org/memoization-using-decorators-in-python/)"""


# factorial program, non memoized
def facto(num):
	return 1 if num == 1 else num * facto(num - 1)


print(facto(5))  # 120
"""------------------------------------------------------------------------------------"""


# memoized factorial, function f passed as parameter
def memoize_factorial(f):
	memory = {}
	
	# This inner function has access to memory and 'f'
	# memory will be saved between function calls
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
		return memory[num]
	
	return inner


@memoize_factorial
def facto(num):
	return 1 if num == 1 else num * facto(num - 1)


print(facto(5))  # 120
# facto(10) will compute 10,9,8,7,6 and then retrieve from memory 5,4,3,2,1 since facto(5) went before
