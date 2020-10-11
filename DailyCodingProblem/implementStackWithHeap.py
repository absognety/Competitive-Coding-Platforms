"""
Daily Coding Problem #154

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements 
the following methods:
    1. push(item), which adds an element to the stack
    2. pop(), which removes and returns the most recently added 
    element (or throws an error if there is nothing on the stack)
    
Recall that a heap has the following operations:
    1. push(item), which adds a new key to the heap
    2. pop(), which removes and returns the max value of 
    the heap
    
"""

import heapq
import collections

class MaxHeapObj(object):
    def __init__(self, val): 
        self.val = val
    def __lt__(self, other): 
        return self.val > other.val 
    def __eq__(self, other): 
        return self.val == other.val
    def __str__(self): 
        return str(self.val)

#For example:
# maxh = []
# heapq.heappush(maxh, MaxHeapObj(23))
# heapq.heappush(maxh, MaxHeapObj(2))
# heapq.heappush(maxh, MaxHeapObj(234))
# heapq.heappush(maxh, MaxHeapObj(230))
# heapq.heappush(maxh, MaxHeapObj(20))
# x = maxh[0].val  # fetch max value
# x = heapq.heappop(maxh).val  # pop max value

class stackAPI():
    def __init__(self,heap):
        self.heap = heap
        self.pushed = []
        
    def push(self,item):
        self.pushed.append(item)
        heapq.heappush(self.heap,MaxHeapObj(item))
        
    def heap_pop(self):
        ele = heapq.heappop(self.heap).val
        return ele
        
    def pop(self):
        if not self.heap:
            raise Exception("Stack Underflow")
        inds = []
        recent = self.pushed[-1]
        for i,c in enumerate(self.heap):
            if c.val == recent:
                inds.append(i)
        self.pushed.pop()
        print (inds)
        if 0 in inds:
            return self.heap_pop()
        else:
            for index in inds:
                C = self.heap.pop(index)
                break
            temp = collections.deque(self.heap)
            temp.appendleft(C)
            self.heap = list(temp)
            return self.heap_pop()
        
#Test the implementation
#[2,3,4,0,1,10,25,22,18,-1,8]
s = stackAPI([])
s.push(2)
s.push(3)
s.push(4)
s.push(0)
s.push(1)
s.push(10)
s.push(25)
s.push(22)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()