from TreeNode import *
class BinarySearchTree:

    def __init__(self):
        self.root = None # later initialized to be a TreeNode object
        self.size = 0

    # my answer
    def nodeCount(self, t): # executes n times because it doesn't visit None
        count = 0
        if t.hasLeftChild():
            count += self.nodeCount(t.leftChild)
        if t.hasRightChild():
            count += self.nodeCount(t.rightChild)
        return count + 1

    # The answer on the exam
    def nodeCount_ans(self, t): # executes 2n+1 times because it visits None nodes
        if t is None:
            return 0
        return 1 + self.nodeCount_ans(t.leftChild) + self.nodeCount_ans(t.rightChild)

    # my solution (yeah, mine is sex)
    def findValue(self, i, t): # i is the search value, t is the root
        if t is None:  # we went to a child node that DNE
            return
        if t.key == i: # we found it
            return t   # return the node that has it
        return self.findValue(i, t.leftChild) or self.findValue(i, t.rightChild)

    # the exam answer
    def findValue_ans(self, i, t):
        if t is None:
            return None
        if t.key == i:
            return t
        else:
            l = self.findValue_ans(i, t.leftChild)
            r = self.findValue_ans(i, t.rightChild)
            if l != None:
                return l
            elif r != None:
                return r
            else:
                return None





    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get_Node(self,key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def find_path(self, element_1_key, element_2_key):
        """This function calls _find_path()"""
        ### You can use the variables given here or define your own (to be used in _find_path()), below this line (line 129 till line 160)
        self.e1 = self.get_Node(element_1_key) # Get the node corresponding to key
        self.e2 = self.get_Node(element_2_key) # Get the node corresponding to key

        if (not self.e1) or (not self.e2):
            print("Keys Not present!!")
            return

        self.list_1 = [] # To append keys for moving up parents
        self.list_2 = [element_2_key] # To append keys when moving down children

        # To indicate which element is greater. To be used in constructing path
        if element_1_key < element_2_key:
            nature = 0
        elif element_1_key is element_2_key:
            print(self.list_1)
            return [self.list_1, 1]
        else:
            nature = 1
        self.steps = 0
    ### Above this line you can use the variables given here or define your own function (line 129 till line 160)

        # Don't change return
        return self._find_path(self.e1, self.e2, nature) # pass nodes and nature

    def _find_path(self, element_1, element_2, nature):
        self.steps+= 1 # count steps
        if element_1.key == element_2.key: # check if the node it moved to is the right node
            list_path = self.list_1 + self.list_2 # combine parent trace and children trace
            return [list_path, self.steps]
        if nature == 0: # e1 < e2 so e1 must be to the left
            if element_2.hasLeftChild(): # if e2 has a left child become that node
                self.list_2.append(element_2.leftChild.key) # add the key
                n = 0 if element_1.key < element_2.leftChild.key else 1 # set nature for next comparison
                return self._find_path(element_1, element_2.leftChild, n)
            else:
                self.steps = 1 # reset shortest step counter
                self.list_1.append(self.e2.key) # append the self.element_2.key (and later, parents above)
                self.e2 = self.e2.parent # move up for next comparison
                self.list_2 = [] # reset the child list
                self.list_2.append(self.e2.key) # append the first key that started the branch
                n = 0 if element_1.key < self.e2.key else 1 # set nature for next comparison
                return self._find_path(element_1, self.e2, n)
        # nature == 1
        elif nature == 1: # e1 > e2 so e1 must be to the right
            if element_2.hasRightChild(): # if e2 has a right child become that node
                self.list_2.append(element_2.rightChild.key) # add the key
                n = 0 if element_1.key < element_2.rightChild.key else 1 # set nature for next comparison
                return self._find_path(element_1, element_2.rightChild, n)
            else:
                self.steps = 1 # reset shortest step counter
                self.list_1.append(self.e2.key) # append the self.element_2.key (and later, parents above)
                self.e2 = self.e2.parent # move up for next comparison
                self.list_2 = [] # reset the child list
                self.list_2.append(self.e2.key) # append the first key that started the branch
                n = 0 if element_1.key < self.e2.key else 1 # set nature for next comparison
                return self._find_path(element_1, self.e2, n)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)