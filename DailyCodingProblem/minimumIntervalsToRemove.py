"""
Daily Coding Problem #191

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number 
of intervals you need to remove to make the rest of the intervals 
non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't 
be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), 
return 1 as the last interval can be removed and the first two 
won't overlap.

The intervals are not necessarily sorted in any order.

"""

def min_intervals_remove(intervals):
    counter = 0
    for i in range(len(intervals)):
        for j in range(i+1,len(intervals)):
            if intervals[i] == intervals[j]:
                continue
            a = set(range(intervals[i][0],intervals[i][1]+1))
            b = set(range(intervals[j][0],intervals[j][1]+1))
            if (len(a.intersection(b)) == 1) & \
               (intervals[i][1] == intervals[j][0]):
                   continue
            if (len(a.intersection(b)) >= 1):
                counter += 1
    return counter
    
if __name__ == '__main__':
    arr = []
    for tcase in range(int(input())):
        n = int(input())
        for c in range(n):
            pair = list(map(int,input().strip().split())) 
            arr.append((pair[0],pair[1]))
        print (min_intervals_remove(arr))