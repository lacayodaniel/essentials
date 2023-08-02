
def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1] # move the element on the left to the right
            position -= 1                         # keep moving left

        alist[position] = currentvalue

