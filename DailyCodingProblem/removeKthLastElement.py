"""
Daily Coding Problem #26

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element 
from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively 
expensive.

Do this in constant space and in one pass.

"""

class Node(object):
    def __init__(self,dataVal):
        self.data = dataVal
        self.next = None
        
    def getData(self):
        return (self.data)
    
    def setData(self,val):
        self.data = val
    
    def getNextNode(self):
        return (self.next)
    
    def setNextNode(self,nextVal):
        self.next = nextVal
        
class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        self.lastNode = None
        self.size = 0
        
    def getSize(self):
        return self.size
        
    def insertNode(self,data):
        if self.head == None:
            self.head = Node(data)
            self.lastNode = self.head
            self.size+=1
        else:
            newNode = Node(data)
            self.lastNode.next = newNode
            self.lastNode = newNode
            self.size+=1
    
    def deleteNode(self,position,n):
        assert position <= n,"k is not smaller than length of the list"
        temp = self.head
        if temp is not None:
            if position == 1:
                self.head = temp.next
                temp = None
                return
        s = 1
        while (temp is not None):
            if s == position:
                break
            prev = temp
            s += 1
            temp = temp.next
        prev.next = temp.next
        temp=None
    
    def traversal(self):
        T = self.head
        while T is not None:
            print (T.data,end = " ")
            T = T.next
            
if __name__ == '__main__':
    k = int(input())
    arr = list(map(int,input().strip().split()))
    n = len(arr)
    llist = LinkedList()
    
    for e in arr:
        llist.insertNode(e)
        
    llist.traversal()
    
    llist.deleteNode(n-k+1,n)
    
    llist.traversal()