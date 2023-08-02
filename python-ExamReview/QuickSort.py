def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
        # move leftmark to where alist[leftmark] > pivotvalue
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
        # move rightmark to where alist[rightmark] < pivotvalue
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
        # swap alist[leftmark] with alist[rightmark]
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

    # swap pivot with alist[rightmark] (values left of pivot < pivot < values right of pivot)
   temp = pivotvalue
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

    # indicate where to split the list to do it again
   return rightmark
