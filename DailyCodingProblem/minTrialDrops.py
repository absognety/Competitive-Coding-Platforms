"""
Daily Coding Problem #230

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k 
floors. Your task is to find the lowest floor that will cause an 
egg to break, if dropped from that floor. Once an egg breaks, it 
cannot be dropped again. If an egg breaks when dropped from the 
xth floor, you can assume it will also break when dropped from 
any floor greater than x.

Write an algorithm that finds the minimum number of trial drops 
it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the 
egg at every floor, beginning with the first, until we reach the 
fifth floor, so our solution will be 5.

"""
import math
#Solution using recursion
def minimum_trial_drops(n,k):
    """
    Input:
       n: number of identical eggs
       k: number of floors in the building
    Output:
       result: Minimum number of trials
    """
    #If number of floors is 1 or 0
    if (k == 1 or k==0):
        return k
    #if number of eggs is equal to 1, then it is given k
    if n == 1:
        return k
    minimum = math.inf
    for x in range(1,k+1):
        res = max(minimum_trial_drops(n-1,x-1),
                  minimum_trial_drops(n,k-x))
        if res < minimum:
            minimum = res
    return minimum + 1

if __name__ == '__main__':
    n = 1
    k = 5
    print (minimum_trial_drops(n,k))
    n = 2
    k = 10
    print (minimum_trial_drops(n,k))