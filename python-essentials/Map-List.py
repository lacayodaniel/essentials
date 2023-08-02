
"""Dictionary methods make things wayyyy easier"""
some_dict = {1:1, 2:4, 3:9}
x = 5

# Bad method
if x in some_dict:
    y = some_dict[x]
else:
    y = None

# Alternative
y = some_dict.get(x,None) # y = d[x] if x in d else None

# Bad method
if x not in some_dict:
    some_dict[x] = []
some_dict[x].append(y)

# Alternative
some_dict.setdefault(x,[]).append(y) # if x not in d, then d[x] = [y]



"""Map is a high-order function because it applies a function
to each member for a any collection passed"""
import functools

# filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst)) # [1,3,5,7,9,...,19]

# filtering odd square which are divisible by 5
lst = filter(lambda x : x % 5 == 0, [x ** 2 for x in range(1, 11) if x % 2 == 1])
print (list(lst)) # [25]

# filtering negative numbers
lst = filter((lambda x: x < 0), range(-5,5))
print (list(lst)) # [-5,-4,-3,-2,-1]

# implementing max() function, using
print (functools.reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15])) # 100

# sqaure all elements
print(list(map(lambda x: x**2, [1,2,3,4,5]))) # [1, 4, 9, 16, 25]

"""Lambda: Anonymous Functions
https://www.geeksforgeeks.org/python-lambda/?ref=lbp"""
# add an int x to every element in array a
addacr = lambda x,a: [i+x for i in a]
print(addacr(10,[1,2,3])) # [11,12,13]

# the above, but with list slicing
example = [1,2,3,4,5]
example[1:4] = addacr(10,example[1:4])
print(example) # [1,12,13,14,5]


"""List slicing
https://www.geeksforgeeks.org/python-arrays/?ref=lbp"""
arr = [1,2,3,4,5]

# reverse list
arr[::-1]

# last element
arr[-1] #5

# all elements
arr[:] or arr[::] or arr # [1,2,3,4,5]

# second to last element inclusive
arr[1:]

# second to fourth element inclusive
arr[1:4] # [2,3,4]

# list replacement
arr[1:4] = [9]*(4-1) # element you want to replace * number of replacements
print(arr) # [1,9,9,9,5]
