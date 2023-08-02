
import abc
"""
https://www.geeksforgeeks.org/abstract-classes-in-python/?ref=lbp
"""
class parent:
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))
