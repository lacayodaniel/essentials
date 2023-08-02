from QueueExample import *
from InsertionSort import *
from BST import *
from BSTAsList import *
from BinarySearch import *
from LinksAndPointers import *
from OrderedList import *
from QuickSort import *
from BSTAVL import *

def queue_question(): # in QueueExample.py
    print("Question 1")
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    q.enqueue(2.8)
    q.dequeue()
    q.dequeue()
    print(q)

def insertion_question(): # in InsertionSort.py
    print("Question 2")
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 100]
    insertionSort(alist)
    print(alist)

def BST_question(): # in TreeNode.py and BST.py
    print("Question 7")
    mytree = BinarySearchTree()

    mytree[4] = "red"
    mytree[8] = "yellow"
    mytree[6] = "blue"
    mytree[3] = "pew"
    mytree[5] = "green"
    mytree[7] = "ow"
    mytree[1] = "wow"
    mytree[2] = "cool"

    print(mytree[6]) # expected: blue
    print(mytree[2]) # expected None
    path_list_steps = mytree.find_path(5, 7)
    print(path_list_steps[0], path_list_steps[1]) # expected [7, 6, 5] 3
    print(len(mytree)) # expected 6
    # del mytree[6]
    print(len(mytree)) # expected 5
    path_list_steps = mytree.find_path(5, 7)
    print(path_list_steps[0], path_list_steps[1])  # expected [7, 5] 2

    print("------ Exam 2 ------")
    print(mytree.nodeCount(mytree.root))
    print(mytree.nodeCount_ans(mytree.root))
    print(mytree.findValue(8, mytree.root))
    print(mytree.findValue_ans(4, mytree.root))


def RMost_LMost_question():
    alist = [5, 10, 9, 6, 8, 3, 1, 4, 2, 7]
    print(findRightMost(alist, 0, 10))
    print(findLeftMost(alist, 0, 10))

def BinarySearch_question():
    testlist = [36,32,29,26,25,21,18,17,14,12,11,9,8,2,1]
    search = 32
    print(binarySearch(testlist, search))

def pointers_question():
    a = SomeObject(3)
    b = SomeObject(4)
    c = SomeObject(5)

    # Problem a)
    a.link = c
    b.link = a
    c.link = b
    print(a.link.x, b.link.x, c.link.x)

    # Problem b)
    a.link = b.link
    b.link = c.link
    c.link = a.link
    print(a.link.x, b.link.x, c.link.x)

    # Problem c)
    a.link.x = 6
    b.link.link.x = 7
    c.link.link.link.x = 8
    print(a.link.x, b.link.x, c.link.x)

def OL_question():
    ol = OrderedList()
    ol.add(1)
    ol.add(2)
    ol.reverseOrder()
    print(ol)
    ol.add(50)
    print(ol)
    ol.reverseOrder()
    print(ol)
    ol.remove(50)
    ol.add(3)
    ol.add(4)
    print(ol)
    ol.remove(1)
    print(ol)
    ol.add(1)
    print(ol)

def testQuickSort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 97, 20]
    quickSort(alist)
    print(alist)

def testBSTAVL():
    avl = AvlTree()
    avl[29] = "cool"
    avl[28] = "snazzy"
    avl[27] = "bitch"
    avl[26] = "kms"
    avl[25] = "dub"
    print(avl.root.key)
    print(avl.root.rightChild.rightChild.key)
    print(avl.root.balanceFactor)
    print(avl.size)


if __name__ == '__main__':
    queue_question()
    # insertion_question()
    # BST_question()
    # RMost_LMost_question()
    # BinarySearch_question()
    # pointers_question()
    # OL_question()
    # testQuickSort()
    # testBSTAVL()












