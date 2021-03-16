"""
Given a stack, sort it using recursion. Use of any loop constructs like 
while, for..etc is not allowed. We can only use the following ADT 
functions on Stack S: 

is_empty(S)  : Tests whether stack is empty or not.
push(S)         : Adds new element to the stack.
pop(S)         : Removes top element from the stack.
top(S)         : Returns value of the top element. Note that this
               function does not remove element from the stack.
Example: 

Input:  -3  <--- Top
        14 
        18 
        -5 
        30 

Output: 30  <--- Top
        18 
        14 
        -3 
        -5 
"""
def sortedInsert(q:list,element:int):
    if (len(q) == 0):
        q.append(element)
        return
    elif (len(q) != 0) and (element > q[-1]):
        q.append(element)
        return
    temp = q.pop()
    sortedInsert(q, element)
    q.append(temp)
        
def sort_stack(q):
    if len(q) > 0:
        temp = q.pop()
        sort_stack(q)
        sortedInsert(q, temp)
    
if __name__ == '__main__':
    q = []
    q.append(30)
    q.append(-5)
    q.append(18)
    q.append(14)
    q.append(-3)
    print (q)
    sort_stack(q)
    print (q)