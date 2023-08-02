
"""
The yield statement suspends function’s execution and sends a value
 back to the caller, but retains enough state to enable function to
 resume where it is left off. When resumed, the function continues
 execution immediately after the last yield run.
 https://www.geeksforgeeks.org/generators-in-python/?ref=lbp
 """
# example function continues after last yield
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)
""" output
1
2
3
"""
"""-----------------------------------------------------------------------"""
# the above example, but using .next()
x = simpleGeneratorFun()
print(next(x)) # 1
print(next(x)) # 2
print(next(x)) # 3
"""-----------------------------------------------------------------------"""
# squares example
def nextSquare():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

for num in nextSquare():
    if num > 25:
         break
    print(num)
""" output
1
4
9
16
25
"""
