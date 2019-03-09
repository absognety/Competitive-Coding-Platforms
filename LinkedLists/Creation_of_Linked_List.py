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
    
    def traversal(self):
        T = self.head
        while T is not None:
            print (T.data,end = " ")
            T = T.next