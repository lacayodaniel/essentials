from BST import *

class AvlTree(BinarySearchTree):
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                # place the node in the correct place and update the balFact for that node
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                # place the node in the correct place and update the balFact for that node
                self.updateBalance(currentNode.rightChild)

    # Confident this method works as intended, recursively updates
    # the balFact from the inserted node up to the root.
    # If the balfact is too unbalanced, then it calls rebalance
    def updateBalance(self, node):
        if (node.balanceFactor > 1) or (node.balanceFactor < -1):
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            # see which case we have
            # Right Left
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            # Left Left
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            # Left Right
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            # Right Right
            else:
                self.rotateRight(node)

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        # rotRoot.balanceFactor = 1 + max(rotRoot.leftChild.balanceFactor,
        #                  rotRoot.rightChild.balanceFactor)
        # newRoot.balanceFactor = 1 + max(newRoot.leftChild.balanceFactor,
        #                                 newRoot.rightChild.balanceFactor)
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.blanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        # rotRoot.balanceFactor = 1 + max(rotRoot.leftChild.balanceFactor,
        #                                 rotRoot.rightChild.balanceFactor)
        # newRoot.balanceFactor = 1 + max(newRoot.leftChild.balanceFactor,
        #                                 newRoot.rightChild.balanceFactor)
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

