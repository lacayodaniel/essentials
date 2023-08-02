from Fib import *
from QuestionThree import *
from Exam import *
from COV19Library import *
from AVLTree import *
import random
import time


def fib():
    fib = Fibonacci()
    print(fib.F(4))
    print(fib.fact(6))

def q3():
    t = Tree(10)

def question1():
    q1 = Question1()
    A = [1,2,3,4,5,6]
    print(q1.reverseArray(A, 0, 5))

def BSTAVL_covid_example():
    lib = COV19Library()
    lib.LoadData("cov19_city.csv")
    print(lib.size)  # should be 942
    print(lib.linearSearch("11940", "id"))  # should be Athens
    print(lib.linearSearch("Winona", "name"))  # should be Winona
    # for each in lib.cityArray: print(each)
    print(lib.cityArray[-1])  # should be Angola
    print(lib.isSorted)  # should be False
    lib.quickSort()
    print(lib.isSorted)  # should be True
    print(lib.cityArray[-1])  # should be Zanesville
    lib.buildBST()
    print(lib.getHeight(lib.root))  # should be 12
    print(lib.searchBST("34980"))  # should be Nashville; Note there was no cstate in the spreadsheet

    print("Library size (number of nodes): {}".format(lib.size))
    print("First city_node: {}".format(lib.cityArray[0]))
    print("Last city_node: {}".format(lib.cityArray[-1]))
    print("Root city_node: {}".format(lib.root))

def BST_real_ex():
    data = [5, 3, 10, 2, 4, 7, 11, 1, 6, 9, 12, 8]
    avl = AVLTree()
    avl.buildBST(data)
    print("size: {} check: {}".format(avl.size, avl.size - 12))
    print("root: {} check: {}".format(avl.root, avl.root.key - 5))
    print("node: {} check: {}".format(avl.root.rightChild.leftChild.rightChild.leftChild,
                                        avl.root.rightChild.leftChild.rightChild.leftChild.key - 8))
    print("left most node: {} check: {}".format(avl.getLeftMost(avl.root), avl.getLeftMost(avl.root).key - 1))
    print("right most node: {} check: {}".format(avl.getRightMost(avl.root), avl.getRightMost(avl.root).key - 12))

    print(avl)
    print("target: {} check:".format(avl.remove(7))) #, avl.remove(7).key - 7))
    print(avl)
    print(avl.root)
    print(avl.root.rightChild.leftChild.leftChild)



if __name__ == '__main__':
    # fib()
    # question1()
    BST_real_ex()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
