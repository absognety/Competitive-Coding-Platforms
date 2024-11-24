"""
Split the list of N elements into N/2 pairs such that sum of each pair is odd 
and no one element in a pair is common between any set of pairs - any element exists in exactly one pair
"""
import itertools
def solution(A):
	all_pairs = list(itertools.combinations(A, 2))
	tracker = set()
	result = list()
	for t in all_pairs:
		if len(result) == 0:
			if sum(t) % 2 != 0:
				result.append(t)
		else:
			for pair in result:
				tracker = tracker.union(set(pair))
			if not tracker.intersection(set(t)):
				if sum(t) % 2 != 0:
					result.append(t)
	print (result)
	final = list()
	for r in result:
		final.extend(list(r))
	if (set(final) == set(A)) & (len(final) == len(A)):
		return True
	else:
		return False
