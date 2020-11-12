"""
Daily Coding Problem #208

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list 
so that all nodes less than k come before nodes greater than or equal 
to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, 
the solution could be 1 -> 0 -> 5 -> 8 -> 3.

"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist(object):
    def __init__(self,head=None):
        self.head = head
        self.lastNode = None
        self.size = 0

    def getSize(self):
        return self.size

    def insertNode(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.lastNode = self.head
            self.size += 1
        else:
            newNode = Node(data)
            self.lastNode.next = newNode
            self.lastNode = newNode
            self.size += 1
    
    def traversal(self):
        T = self.head
        while T is not None:
            print (T.data,end = " ")
            T = T.next
        print ("\n")

def partitionLinkedList(head,k):
    lesser = []
    greater = []
    T = head
    while T is not None:
        if T.data < k:
            lesser.append(T.data) 
        elif T.data > k:
            greater.append(T.data)
        T = T.next
    after_rearrange = lesser + greater + [k]
    new_linked_list = Linkedlist()
    for r in after_rearrange:
        new_linked_list.insertNode(r)
    new_linked_list.traversal()

if __name__ == '__main__':
    k = 3
    ll = Linkedlist()
    ll.insertNode(5)
    ll.insertNode(1)
    ll.insertNode(8)
    ll.insertNode(0)
    ll.insertNode(3)
    partitionLinkedList(ll.head,k)

    k = 20
    ll2 = Linkedlist()
    ll2.insertNode(21)
    ll2.insertNode(19)
    ll2.insertNode(29)
    ll2.insertNode(34)
    ll2.insertNode(18)
    ll2.insertNode(10)
    ll2.insertNode(9)
    partitionLinkedList(ll2.head,k)