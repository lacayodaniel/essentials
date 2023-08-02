import sys
import math
from math import factorial as f
import functools
from functools import reduce
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import time
import numpy as np


# n choose k = n! / ( k!(n-k)! )
def c(n, k):
	return f(n) / (f(k) * f(n - k))


# return a simplified fraction
def simplify(n):
	return str(Fraction(n))


# convert inches to cm
def in2cm(x, f=0.0):
	if type(x) is str:
		x = int(x)
	
	if type(f) is str:
		f = eval(f)
	
	return 2.54 * (x + f)


# memoized factorial, function f passed as parameter
def memoize_factorial(f):
	memory = {}
	
	# This inner function has access to memory and 'f'
	# memory will be saved between function calls
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
		return memory[num]
	
	return inner


@memoize_factorial
def facto(num):
	return 1 if num == 1 else num * facto(num - 1)


def poisson(i, y):
	i = int(i)
	y = int(y)
	if i <= 0:
		return 0
	return ((math.e ** (-y)) * (y ** i)) / facto(i)


# 20 times faster than v2
# 30% faster than than v3
def freq_of_max(cars, carQ):
	carQ.sort(reverse=True)
	record_max = max(cars[carQ[0] - 1:])
	record_freq = cars[carQ[0] - 1:].count(record_max)
	ans = [record_freq]
	for i in range(len(carQ) - 1):
		# check if the next lookahead array == previous lookahead array
		# speed up duplicate entries in carQ
		if carQ[i + 1] == carQ[i]:
			ans.append(record_freq)  # ans[i+1] = ans[i]
			continue
		# check if max(lookahead) is relevant
		# prune next lookahead array if max is less than record_max
		curr_max = max(cars[carQ[i + 1] - 1:carQ[i] - 1])
		if curr_max < record_max:  # max(next subarray) < max(current subarray)
			ans.append(record_freq)
			continue
		curr_freq = cars[carQ[i + 1] - 1:carQ[i] - 1].count(curr_max)
		if curr_max == record_max:
			record_freq += curr_freq  # next sub array freq + current sub array freq
		else:  # curr_max > record_max
			record_max = curr_max
			record_freq = curr_freq  # next sub array freq only
		ans.append(record_freq)
	return ans


def freq_of_max_2(carsParked, carQuantity):
	return [carsParked[i - 1:].count(max(carsParked[i - 1:])) for i in carQuantity]


def freq_of_max_3(carsParked, carQuantity):
	carQ = carQuantity
	carQ.sort(reverse=True)
	dcount = dict(Counter(carsParked[carQ[0] - 1:]))
	record_max = max(dcount.keys())
	record_count = dcount[record_max]
	ans = [record_count]
	for i in range(len(carQ) - 1):
		if carQ[i + 1] == carQ[i]:
			ans.append(ans[-1])
			continue
		curr_max = max(carsParked[carQ[i + 1] - 1:carQ[i] - 1])
		max_count = carsParked[carQ[i + 1] - 1:carQ[i] - 1].count(curr_max)
		if curr_max > record_max:
			record_max = curr_max
			dcount[curr_max] = max_count
			record_count = max_count
		elif curr_max == record_max:
			dcount[curr_max] += max_count
			record_count = max_count
		ans.append(dcount[record_max])
	return ans


if __name__ == '__main__':
	if sys.argv[1] == "choose":
		print("{}".format(c(int(sys.argv[2]), int(sys.argv[3]))))
	elif sys.argv[1] == "calc":
		result = eval("".join(sys.argv[2:]))
		print("{} ({:.4})".format(simplify(result), float(result)))
	elif sys.argv[1] == "test":
		a1 = list(np.random.randint(1, 900, size=100000))
		b1 = list(np.linspace(1, 10000, num=10000, dtype=int))  # list(np.random.randint(1, 950, size=1000))
		start = time.time()
		a = freq_of_max(a1, b1)
		print(time.time() - start)
		start = time.time()
		c = freq_of_max_3(a1, b1)
		print(time.time() - start)
		start = time.time()
		b = freq_of_max_2(a1, b1)
		print(time.time() - start)
		print(a == b, b == c, a == c)
	elif sys.argv[1] == "in2cm":
		print(in2cm(sys.argv[2], sys.argv[3]))
	elif sys.argv[1] == "poisson":
		print(poisson(sys.argv[2], sys.argv[3]))

# # 20 times faster than v2
# # 30% faster than than v3
# def freq_of_max(cars, carQuantity):
#     carQ = carQuantity
#     carQ.sort(reverse=True)
#     record_max = max(cars[carQ[0]-1:])
#     record_count = cars[carQ[0]-1:].count(record_max)
#     ans = [record_count]
#     for i in range(len(carQ)-1):
#         if carQ[i+1] == carQ[i]:
#             ans.append(ans[-1])
#             continue
#         curr_max = max(cars[carQ[i+1]-1:carQ[i]-1])
#         if curr_max > record_max: # this if block could be faster, change order
#             record_max = curr_max
#             added_cars = (cars[carQ[i+1]-1:carQ[i]-1]).count(record_max)
#             ans.append(added_cars)
#         elif curr_max == record_max:
#             record_count += (cars[carQ[i+1]-1:carQ[i]-1]).count(record_max)
#             ans.append(record_count)
#         else:
#             ans.append(ans[-1])
#     return ans
