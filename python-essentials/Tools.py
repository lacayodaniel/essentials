import argparse

"""How to quickly find all permutations of a string"""
from itertools import permutations


def calc_permutations(word, n, prttyp):
	ans = ["".join(permutation) for permutation in list(permutations(word, n))]  # [('H', 'A'),...]
	ans.sort()  # alphebetize
	if prttyp:
		for i in ans:
			print(i)  # print all permutations
		print("# of permutations", len(ans))  # number of permutations on word given constraint n
	return ans


"""How to count occurrances of components of a whole. i.e. ccca c:3 a:1"""
from collections import Counter


def max_unique(lst):  # max_unique([9, 0, 1, 2, 5, 8, 6, 7, 5, 3, 0, 9]))
	"""Returns the largest element of a list that appears only once"""
	val_counts = dict(Counter(lst))  # {list element : count}
	# filter for elements with 1 occurance and return the max
	return max(list(filter(lambda x: val_counts[x] == 1, val_counts)))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('tool', choices=['perm', 'fc'])
	parser.add_argument('--word', type=str)
	parser.add_argument('--n', type=int)
	parser.add_argument('--lst', type=str, nargs='+') # '+' means 1 or more '*' means 0 or more
	args = parser.parse_args()
	
	for f in [args.tool]:
		if f == 'perm':  # permutation function
			print(calc_permutations(args.word, args.n, False))
		elif f == 'fc':  # frequency count function
			print(max_unique(args.lst))
