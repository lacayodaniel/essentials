from Node import *
from Stack import *
class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.stack = Stack()
        self.vis = []

    def buildBST(self, keys): # takes an array of keys and creates a balanced BST
        for key in keys:
            self.insert(key)
        return

    def insert(self, key): # creates a node and calls _insert
        self.root = self._insert(self.root, key, Node(key))
        self.size += 1

    def _insert(self, root, key, node):
        # place node in the correct place
        if root is None:
            return node
        # search for where to put the node
        elif key < root.key:
            root.leftChild = self._insert(root.leftChild, key, node)
        else:
            root.rightChild = self._insert(root.rightChild, key, node)
        # calculate height and balance for previous node
        root.height = self.calculateHeight(root)
        balance = self.getBalance(root)
        return self.updateBalance(balance, key, root) # returns the root node for all nodes below root



    def updateBalance(self, balance, key, node):
        # if the node is unbalanced, then see which case we have
        if balance > 1:
            # Left Right
            if key > node.leftChild.key:
                node.leftChild = self.leftRotate(node.leftChild)
            # Right
            return self.rightRotate(node) # becomes root for next pass
        if balance < -1:
            # Right Left
            if key < node.rightChild.key:
                node.rightChild = self.rightRotate(node.rightChild)
            # Left
            return self.leftRotate(node) # becomes root for next pass
        # no balancing needed
        return node

    def remove(self, key):
        '''
        1. Find target node for deletion (if it exists)
            1.1 In searching for target, keep track of all visited nodes as a stack (only need previous node?)
            1.2 Find target's left most child as left_most_node using stack
            1.3 Find left_most_nodes's right most child as right_most_node using stack
        2. Select target's rightChild as replacement
        3. Set parent node's child (determine which) as replacement (1.1, first pop)
        4. Set right_most_node's rightChild as replacement's leftChild (1.3, first pop)
        5. Set replacement's leftChild as target's leftChild
        6. Delete target
        7. Start updating balance for nodes in stack 1.3
        8. Start updating balance for nodes in stack 1.2
        9. Start updating balance for nodes in stack 1.1
        '''
        target = self.trackBST(key)
        if target is None:
            return
        # if self.stack.size == 0: # the root is being deleted
        parent = self.stack.peek()
        replacement = target.rightChild
        direction = True if parent.leftChild == target else False
        if replacement is None and target.leftChild is None: # there is no child to replace target
            if direction:
                parent.leftChild = None
                # need to go through stack updating heights and balancing
            else:
                parent.rightChild = None
                # need to go through stack updating heights and balancing
        elif replacement is None:
            # there is no right child to replace target
            # update parent's child with target's left child
            if direction:
                parent.leftChild = target.leftChild
            else:
                parent.rightChild = target.leftChild
        else: # replacement exists
            if direction:
                parent.leftChild = replacement
            else:
                parent.rightChild = replacement
            # find target's leftmost
            # find rightmost from leftmost
            if target.leftChild is not None:
                leftmost = self.getLeftMost(target)
                if leftmost.rightChild is not None:
                    rightmost = self.getRightMost(leftmost)
                    rightmost.rightChild = replacement.leftChild # doesn't matter if leftChild is None
                    # at this point, stack has all nodes from root to rightmost
                    lkey = replacement.leftChild.key
                    for i in range(self.stack.size):
                        node = self.stack.pop()
                        node.height = self.calculateHeight(node)
                        balance = self.getBalance(node)
                        self.root = self.updateBalance(balance, lkey, node)
        return self.root


        #return target
    def trackBST(self, key):
        # search the BST based on a node id
        node = self._trackBST(key, self.root)

        # if the node is None then the node was not found
        if node is None:
            self.stack.clear()
            return None

        return node

    # recursively calls itself on the children nodes in the direction of the key
    # direction is inherint in a
    # BST, key > currentNode.key => search right else: search left
    def _trackBST(self, key, currentNode):
        self.stack.insert(currentNode)
        if not currentNode:
            return None # node not found

        elif currentNode.key == key:
            self.stack.pop() # first node in stack is parent node
            return currentNode # we have a match

        # search left children
        elif key < currentNode.key:
            return self._trackBST(key, currentNode.leftChild)

        # search right children
        else:
            return self._trackBST(key, currentNode.rightChild)

    def getLeftMost(self, node):
        if node.leftChild is not None:
            return self.getLeftMost(node.leftChild)
        self.stack.insert(node)
        return node

    def getRightMost(self, node):
        if node.rightChild is not None:
            return self.getRightMost(node.rightChild)
        self.stack.insert(node)
        return node



    def leftRotate(self, rotRoot):
        # rotate
        #         rot                      new
        #        /   \        =>          /   \
        #       _    new                rot    RC
        #           /   \              /   \
        #         LC     RC           _     LC
        newRoot = rotRoot.rightChild
        newRoot.leftChild, rotRoot.rightChild = rotRoot, newRoot.leftChild
        # calculate heights
        rotRoot.height = self.calculateHeight(rotRoot)
        newRoot.height = self.calculateHeight(newRoot)
        return newRoot # return to _insert

    def rightRotate(self, rotRoot):
        # rotate
        #         rot                      new
        #        /   \        =>          /   \
        #      new    _                 LC     rot
        #     /   \                           /   \
        #   LC     RC                       RC     _
        newRoot = rotRoot.leftChild
        newRoot.rightChild, rotRoot.leftChild = rotRoot, newRoot.rightChild
        # calculate heights
        rotRoot.height = self.calculateHeight(rotRoot)
        newRoot.height = self.calculateHeight(newRoot)
        return newRoot # return to _insert

    def getHeight(self, node):
        # remember; not None => True; not <some_class> => False; None => False
        if node:
            return node.height
        return 0 # node == None

    # balance is height of leftChild node - height of rightChild node
    def getBalance(self, node):
        # remember; not None => True; not <some_class> => False; None => False
        if node:
            return self.getHeight(node.leftChild)\
                   - self.getHeight(node.rightChild)
        return 0 # node == None

    # root is maximum height, the lowest child node has height 1
    def calculateHeight(self, node):
        # use max to find the unbalanced height
        return 1 + max(self.getHeight(node.leftChild),
                       self.getHeight(node.rightChild))

    def searchBST(self, key):
        # search the BST based on a node id
        node = self._searchBST(key, self.root)

        # if the node is not None then the node was found
        if node:
            return node
        return "City not found" # node == None

    # recursively calls itself on the children nodes in the direction of the key
    # direction is inherint in a
    # BST, key > currentNode.key => search right else: search left
    def _searchBST(self, key, currentNode):
        if not currentNode:
            return None # node not found

        elif currentNode.key == key:
            return currentNode # we have a match

        # search left children
        elif key < currentNode.key:
            return self._searchBST(key, currentNode.leftChild)

        # search right children
        else:
            return self._searchBST(key, currentNode.rightChild)

    def inOrder(self, root, k1=0, k2=100):

        # Base Case
        if root is None:
            return

            # Since the desired o/p is sorted, recurse for left
        # subtree first. If root.data is greater than k1, then
        # only we can get o/p keys in left subtree
        if k1 < root.key:
            self.inOrder(root.leftChild, k1, k2)

            # If root's data lies in range, then prints root's data
        if k1 <= root.key and k2 >= root.key:
            self.vis.append(root.key)

            # If root.data is smaller than k2, then only we can get
        # o/p keys in right subtree
        if k2 > root.key:
            self.inOrder(root.rightChild, k1, k2)

    def __str__(self):
        self.inOrder(self.root)
        return "{}".format(self.vis)
