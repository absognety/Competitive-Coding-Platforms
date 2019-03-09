class Node:
    def __init__(self,dataVal):
        self.data = dataVal
        self.next = None
        self.head = None
        
    def getData(self):
        return (self.data)
    
    def setData(self,val):
        self.data = val
    
    def getNextNode(self):
        return (self.next)
    
    def setNextNode(self,nextVal):
        self.next = nextVal
    
class LinkedList:
    def __init__(self,head=None):
        self.head = None
        self.size = 0
        self.lastNode = None
        
    def getSize(self):
        return (self.size)

    def addNode(self,data):
        if self.head == None:
            self.head = Node(data)
            self.lastNode = self.head
            self.size+=1
        else:
            newNode = Node(data)
            self.lastNode.next = newNode
            self.lastNode = newNode
            self.size += 1
    def createList(self,arr,n):
        for i in range(n):
            self.addNode(arr[i])
        return self.head
    def reverseList(self,arr,n):
        self.head = None
        reversed_arr = arr[::-1]
        for i in range(n):
            self.addNode(reversed_arr[i])
        return self.head
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print (tmp.data,end=' ')
            tmp = tmp.next
        print ()
      
##Driver Code
if __name__ == '__main__':
    T = int(input())
    num_elements = int(input())
    arr = input().strip().split()
    linkedList = LinkedList()
    linkedList.createList(arr,num_elements)
    linkedList.printList()
    linkedList.reverseList(arr,num_elements)
    linkedList.printList()
