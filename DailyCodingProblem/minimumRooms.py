"""
Daily Coding Problem #21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should 
return 2.

"""
import itertools
from heapq import heappush,heappop
def min_rooms(intervals):
    if len(intervals) == 1:
        return 1
    pairs = list(itertools.combinations(intervals,2))
    minrooms = 0
    for tup in pairs:
        set1 = set(range(tup[0][0],tup[0][1]))
        set2 = set(range(tup[1][0],tup[1][1]))
        if len(set1.intersection(set2)) > 0:
            minrooms += 1
    return minrooms


def minimum_rooms(intervals):
    if not intervals:
        return 0
    sorted_intervals = sorted(intervals,key=lambda it: (it[0],it[1]))
    cnt = 0
    heap = []
    #print ([(i[0],i[1]) for i in sorted_intervals])
    for tup in sorted_intervals:
        start,end = tup[0],tup[1]
        
        while heap and (heap[0] <= start):
            heappop(heap)
            
        heappush(heap,end)
        cnt = max(len(heap),cnt)
        #print (start,end,heap)
    return cnt

if __name__ == '__main__':
    intervals = [(30, 75), (0, 50), (60, 150)]
    intervals1 = [(0,30),(5,10),(15,20)]
    intervals2 = [(2,7)]
    intervals3 = [(10,30),(5,10),(5,6),(15,20)]
    
    print (min_rooms(intervals1))
    print (min_rooms(intervals2))
    print (min_rooms(intervals3))
    print (min_rooms(intervals))
    
    print (minimum_rooms(intervals1))
    print (minimum_rooms(intervals2))
    print (minimum_rooms(intervals3))
    print (minimum_rooms(intervals))