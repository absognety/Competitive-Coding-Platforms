## Leetcode questions:
### 1. Number of Students unable to eat lunch
Overview
We need to find the number of students who are unable to eat lunch at the school cafeteria.

We are given an array sandwiches that represents a stack of sandwiches, where sandwiches[0] is the sandwich at the top of the stack.

Circular sandwiches are represented with a 0.
Square sandwiches are represented with a 1.
We are also given an array students which represents a queue of students in line at the cafeteria, where students[0] is the first student in the queue.

Students who prefer circular sandwiches are represented with a 0.
Students who prefer square sandwiches are represented with a 1.
Lunch proceeds with the following process:

The first student takes the top sandwich if it matches their preference and leaves the queue, otherwise, they go to the back of the queue. This repeats until none of the students in the queue want to take the top sandwich.

After this, we return the number of students who are unable to eat, which will be the number of students remaining in the queue.

Key Observations:

The number of students and the number of sandwiches are the same.
We cannot change the order of the sandwiches.
The only ways we can modify the order of the students is by giving them sandwiches, which removes them from the queue, or sending them to the back of the queue.

Example 1:  
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]  
Output: 0  
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:  
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]  
Output: 3  


Solution: [NUEL.py](https://github.com/absognety/Competitive-Coding-Platforms/blob/master/LeetCode/NUEL.py)  


### Best Team with No Conflicts  
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.  

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.  

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:  

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]  
Output: 34  
Explanation: You can choose all the players.  

Example 2:  
Input: scores = [4,5,6,5], ages = [2,1,2,1]  
Output: 16  
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.  

Example 3:
Input: scores = [1,2,3,5], ages = [8,9,10,1]  
Output: 6  
Explanation: It is best to choose the first 3 players.  
 

Constraints:  

1 <= scores.length, ages.length <= 1000  
scores.length == ages.length  
1 <= scores[i] <= 106  
1 <= ages[i] <= 1000  
