"""
Daily Coding Problem #141

This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
    
"""

class Stack:
    def __init__(self):
        self.list = [[],[],[]]

    def pop(self, stack_number):
        if len(self.list[stack_number-1]) == 0:
            print ("stack underflow")
            return
        res = self.list[stack_number-1].pop()
        return res

    def push(self, item, stack_number):
        self.list[stack_number-1].append(item)
        
##testing my class
coins = Stack()
coins.push(34, 3)
coins.push(2,1)
coins.push(100,2)
coins.push(101, 2)
coins.push(28,3)
print (coins.list)
coins.pop(3)
coins.pop(1)
coins.pop(1)
print (coins.list)