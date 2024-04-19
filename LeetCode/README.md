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
