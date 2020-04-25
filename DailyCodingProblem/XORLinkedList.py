"""
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
        self.npx = None
        
def XORValue(a,b):
    return Node(a.data ^ b.data)

def insert(head_ref,data):
    # Allocate memory for new node
    new_node = Node(data)
    
    #Since new node is being inserted at the  
    #beginning, npx of new node will always be  
    #XOR of current head and NULL
    new_node.npx = head_ref
    
    #If linked list is not empty, then npx of  
    #current head node will be XOR of new node  
    #and node next to current head
    if head_ref != None:
        
        #*(head_ref)->npx is XOR of NULL and next.  
        #So if we do XOR of it with NULL, we get next 
        head_ref.npx = XORValue(new_node,head_ref.npx)
    head_ref = new_node
    return
    
def printList(head):
    curr = head
    prev = None
    
    while (curr != None):
        print (curr.data)
        next_node = XORValue(prev,curr.npx)
        prev = curr
        curr = next_node
    return
        
if __name__ == '__main__':
    #/* Create following Doubly Linked List  
    #head-->40<-->30<-->20<-->10 */
    head = Node(None)
    insert(head,10)
    insert(head,20)
    insert(head,30)
    insert(head,40)
    
    printList(head)