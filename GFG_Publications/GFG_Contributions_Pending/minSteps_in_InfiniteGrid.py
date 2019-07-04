"""
Given an infinite grid, initial cell position (x, y) and a sequence of other 
cell position which needs to be covered in the given order. The task is to 
find the minimum number of steps needed to travel to all those cells.
Note: Movement can be done in any of the eight possible directions from a 
given cell i.e from cell (x, y) you can move to any of the following eight 
positions:(x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), 
(x+1, y+1), (x, y+1) is possible.

Examples:
    
Input: points[] = [(0, 0), (1, 1), (1, 2)]
Output: 2
Move from (0, 0) to (1, 1) in 1 step(diagonal) and
then from (1, 1) to (1, 2) in 1 step (rightwards)

Input: points[] = [{4, 6}, {1, 2}, {4, 5}, {10, 12}]
Output: 14
Move from (4, 6) -> (3, 5) -> (2, 4) -> (1, 3) ->
(1, 2) -> (2, 3) -> (3, 4) ->
(4, 5) -> (5, 6) -> (6, 7) ->
(7, 8) -> (8, 9) -> (9, 10) -> (10, 11) -> (10, 12)

"""


#Traversing from one point to another point
#storing the minimum number of steps
def traversal_steps(A,B):
    points = list(zip(A,B))
    minSteps = 0
    for p in range(len(points)-1):
        #taking the manhattan distance between x and y-coordinates 
        d1 = abs(points[p][0] - points[p+1][0])
        d2 = abs(points[p][1] - points[p+1][1])
        #adding the maximum among the two to the running steps parameter
        minSteps += max(d1,d2)
    return (minSteps)
 
#Main Driver Code
if __name__ == '__main__':
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    print (traversal_steps(A,B))