class Node:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

class Tree:
    def __init__(self, root=None):
        self.root = Node(root)

    def nodeCount(self, t): # t will be the root node
        return None

