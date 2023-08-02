class Node:
    def __init__(self, key, left=None, right=None): # this could be easily added onto a real object class
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.height = 0

    def __str__(self):
        return "{}".format(self.key)