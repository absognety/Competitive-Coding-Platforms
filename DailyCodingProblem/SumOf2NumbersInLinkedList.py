"""

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each 
node represent a digit in the number. The nodes make up the number 
in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same 
linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1

"""

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
def addBoth(head_a,head_b):
    #code here
    result = LinkedList()
    num1 = ""
    curr_node = head_a
    while curr_node != None:
        num1 += str(curr_node.data)
        curr_node = curr_node.next
    num1 = num1[::-1]
    num2 = ""
    curr_node = head_b
    while curr_node != None:
        num2 += str(curr_node.data)
        curr_node = curr_node.next
    num2 = num2[::-1]
    num = int(num1) + int(num2)
    num = str(num)[::-1]
    for i in num:
        result.append(i)
    return result.head
    
if __name__ == '__main__':
    n_a = int(input())
    a = LinkedList() # create a new linked list 'a'.
    nodes_a = list(map(int, input().strip().split()))
    nodes_a = nodes_a[::-1] # reverse the input array
    for x in nodes_a:
        a.append(x)  # add to the end of the list
    n_b =int(input())
    b = LinkedList()  # create a new linked list 'b'.
    nodes_b = list(map(int, input().strip().split()))
    nodes_b = nodes_b[::-1]  # reverse the input array
    for x in nodes_b:
        b.append(x)  # add to the end of the list
    result_head = addBoth(a.head,b.head)
    printList(result_head)