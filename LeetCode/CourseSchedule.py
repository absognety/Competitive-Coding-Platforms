"""
There are a total of numCourses courses you have to take, labeled from 
0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi 
first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have 
to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 
0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Test case:
5
[[1,4],[2,4],[3,1],[3,2]]

20
[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

"""

#my solution
def isPossible(numCourses,prereqs):
    if len(prereqs) >= 1:
        mapping = dict(prereqs)
        distinct_courses = set()
        distinct_courses.add(prereqs[0][0])
        distinct_courses.add(prereqs[0][1])
        l = 1
        while (l <= len(prereqs)-1):
            a = prereqs[l][0]
            b = prereqs[l][1]
            if len(set([a,b])) == 2:
                intersn = distinct_courses.intersection(set([a,b]))
                if len(intersn) >= 2 and ((b,a) in mapping.items()):
                    return "false"
                distinct_courses.add(a)
                distinct_courses.add(b)
            l += 1
        print (distinct_courses)
        if len(distinct_courses) == numCourses:
            return "true"
        else:
            return "false"
    else:
        return "true"
            
#leetcode solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        # map each course to prereq list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
    
if __name__ == '__main__':
    # Testing my solution
    numCourses = 2
    prereqs = [[1,0]]
    print (isPossible(numCourses,prereqs))
    numCourses = 2
    prereqs = [[1,0],[0,1]]
    print (isPossible(numCourses,prereqs))
    numCourses = 5
    prereqs = [[1,4],[2,4],[3,1],[3,2]]
    print (isPossible(numCourses, prereqs))
    numCourses = 20
    prereqs = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print (isPossible(numCourses, prereqs))
    
    #Leetcode solution results
    solution = Solution()
    print (solution.canFinish(numCourses, prereqs))
    
    numCourses = 5
    prereqs = [[1,4],[2,4],[3,1],[3,2]]
    print (solution.canFinish(numCourses, prereqs))