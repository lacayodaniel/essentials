# this will find the right most and left most "node"
# in a binary tree, if that tree is represented as a list and of course already ordered
def findRightMost(arr, i, n): # treating i as the index and n as the len(arr)
    if (2*i)+2 < n:
        return findRightMost(arr, (2*i)+2, n)
    return i
    # return "Right most index: {}, value: {}".format(i, arr[i])

def findLeftMost(arr, i, n):
    if (2*i)+1 < n:
        return findLeftMost(arr, (2*i)+1, n)
    return i
    # return "Left most index: {}, value: {}".format(i, arr[i])




def findRightMost2(n, alist):
    if (2*n)+2 < len(alist):
        return findRightMost2((2*n)+2, alist)
    return n # n is the index in the array of the RightMostNode

def findLeftMost2(n, alist):
    if (2*n)+1 < len(alist):
        return findLeftMost2((2*n)+1, alist)
    return n # n is the index in the array of the LeftMostNode