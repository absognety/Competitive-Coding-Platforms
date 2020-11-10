"""
Daily Coding Problem #201

This problem was asked by Google.

You are given an array of arrays of integers, where each array
corresponds to a row in a triangle of numbers. For example,
[[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down
one row at a time to an adjacent value, eventually ending with an
entry on the bottom row. For example, 1 -> 3 -> 5. The weight of
the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.

"""
import math

dp = {}
def helper(triangle,i,j):
  if i >= len(triangle):
    return 0
  j = 0 if j < 0 else j
  szt = len(triangle[i])
  j = szt - 1 if j >= szt else j
  if (i,j) not in dp:
    dp[(i,j)] = max(helper(triangle,i+1,j),helper(triangle,i+1,j+1)) + triangle[i][j]
  return dp[(i,j)]
    

def maximum_weight_path(triangle):
  sz = len(triangle[-1])
  res = -1 * math.inf
  for i in range(0,sz):
    res = max(res,helper(triangle,0,i))
  return res

print (maximum_weight_path([[1],[2,3],[1,5,1]]))
tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
dp = {}
print (maximum_weight_path(tri))