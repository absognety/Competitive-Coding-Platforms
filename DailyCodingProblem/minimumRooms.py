"""
Daily Coding Problem #21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should 
return 2.

"""
import itertools
def min_rooms(intervals):
    pairs = list(itertools.combinations(intervals,2))
    minrooms = 0
    for tup in pairs:
        set1 = set(range(tup[0][0],tup[0][1]))
        set2 = set(range(tup[1][0],tup[1][1]))
        if len(set1.intersection(set2)) > 0:
            minrooms += 1
    return minrooms

if __name__ == '__main__':
    intervals = [(30, 75), (0, 50), (60, 150)]
    print (min_rooms(intervals))