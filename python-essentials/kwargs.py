
"""
Note that *args is an array, therefore order is preserved.
*kwargs is a dictionary like {key_word : value}, therefore order is not preserved.
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/?ref=lbp
"""
# simulating a given arguement and any number of remaining arguments
def myFunArgs(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFunArgs('Hello', 'Welcome', 'to', 'GeeksforGeeks')
""" output
First argument : Hello
Welcome
to
GeeksforGeeks
"""
"""--------------------------------------------------------------"""
# *kwargs example
def myFunKwargs(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

myFunKwargs(first ='Geeks', mid ='for', last='Geeks')
""" output (original order is lost)
last == Geeks
mid == for
first == Geeks
"""
