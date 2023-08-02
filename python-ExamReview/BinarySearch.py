def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    if first <= last:
        midpoint = (first + last) // 2
        print(alist[first], alist[last], alist[midpoint])
        if alist[midpoint] == item:
            found = True
        else:
            if item > alist[midpoint]: # this assumes alist is sorted in ascending order
                alist = alist[0:midpoint]
                return binarySearch(alist, item)
            else:
                alist = alist[midpoint + 1:]
                return binarySearch(alist, item)
    return found