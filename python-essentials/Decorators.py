
"""
Decorators and passing functions as arugemnts
https://www.geeksforgeeks.org/decorators-in-python/?ref=lbp
"""
# functions can be treated like objects
def shout(text):
    return text.upper()

print(shout('Hello')) # HELLO
yell = shout
print(yell('Hello')) # HELLO

"""-----------------------------------------------------------------------"""
# functions can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print (greeting)

greet(shout) # HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(whisper) # hi, i am created by a function passed as an argument.

"""----------------------------------------------------------------------"""
# functions can return another function
def create_adder(x):
		def adder(y):
				return x+y
		return adder

add_15 = create_adder(15)
print(add_15(10)) # 25
# in create_adder, x=15, y=10

"""---------------------------------------------------------------------"""
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value
    return inner1

# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

# getting the value through return of the function
print("Sum =", sum_two_numbers(1, 2))
""" output
before Execution
Inside the function
after Execution
Sum = 3
"""
"""--------------------------------------------------------------------"""
# Decorators with parameters
def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])
        return func()

    # returning inner function
    return inner

@decorator(like = "geeksforgeeks")
def my_func():
    print("Inside actual function")
""" output
Inside decorator
Inside inner function
I like geeksforgeeks
Inside actual function
"""
