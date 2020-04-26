"""
# Skeleton of python implementation of C++ code.
pointer programming in python is a bit of challenge.

refer https://github.com/subsr97/daily-coding-problem/blob/master/challenges/xor-linked-list.py

Daily Coding Problem #6

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node 
holding next and prev fields, it holds a field named both, which is an XOR of the next 
node and the previous node. Implement an XOR linked list; it has an add(element) which 
adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have 
access to get_pointer and dereference_pointer functions that converts between nodes 
and memory addresses.

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.both = 0
        
    def __str__(self):
        return str(self.data)
        
class XORLinkedList:
    
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        
    def add(self,element):
        new_node = Node(element)
        if self.head.data == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ get_pointer(new_node)
            self.tail = new_node
            
    def get(self,ind):
        previous = 0
        current = self.head
        for i in range(0,ind-1):
            temp = get_pointer(current)
            current = dereference_pointer(previous^current.both)
            previous = temp
            if current.both == previous and i < ind-2:
                print("Invalid index.")
                return None
        return current

    
if __name__ == '__main__':
    #/* Create following Doubly Linked List  
    #head-->40<-->30<-->20<-->10 */
    xor_list = XORLinkedList()
    
    xor_list.add(10)
    xor_list.add(20)
    xor_list.add(30)
    xor_list.add(40)
    
    print (xor_list.get(2))