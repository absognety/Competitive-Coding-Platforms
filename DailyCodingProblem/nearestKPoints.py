"""
This Problem was asked by LinkedIn

Daily Coding Problem #150

Given a list of points, a central point, and an integer k, find the nearest 
k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the 
central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

"""
import math
def nearestKPoints(arr,p,k):
    """
    Parameters
    ----------
    arr : list
        List of tuples containing all points
    p : tuple
        central point
    k : integer
        given integer

    Returns
    -------
    List of k tuples which are nearest to given p
    
    """
    darr = []
    for c in arr:
        d = math.sqrt((c[0]-p[0])**2 + (c[1]-p[1])**2)
        darr.append(d)
    distance_map = zip(arr,darr)
    k_nearest = sorted(darr)[:k]
    return [x for x,y in distance_map if y in k_nearest]
    
if __name__ == '__main__':
    for tcase in range(int(input())):
        m = int(input())
        arr = []
        while (m > 0):
            point = list(map(int,input().strip().split()))
            arr.append((point[0],point[1]))
            m -= 1
        central_point = list(map(int,input().strip().split()))
        central_point = (central_point[0],central_point[1])
        k = int(input())
        print (nearestKPoints(arr,central_point,k))