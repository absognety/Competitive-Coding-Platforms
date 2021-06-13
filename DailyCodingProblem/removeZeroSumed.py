"""
Daily Coding Problem #417

This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to 
zero. Print out the remaining nodes.

For example, suppose you are given the input 
3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first 
remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
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
        
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')

def remove_linked_lists(head):
    first = head
    all_zero_sumed = []
    while (first != None):
        stack = []
        stack.append(first.data)
        if sum(stack) == 0:
            all_zero_sumed.append(stack)
            stack.clear()
        second = first.next
        temp = stack.copy()
        while (second != None):
            temp.append(second.data)
            if sum(temp) == 0:
                all_zero_sumed.append(temp.copy())
            second = second.next
        first = first.next
    return all_zero_sumed

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(3)
    llist.append(4)
    llist.append(-7)
    llist.append(5)
    llist.append(-6)
    llist.append(6)
    printList(llist.head)
    zero_sumed = remove_linked_lists(llist.head)
    #use regexes to find the linked lists that sum to zero in 
    #the original list and remove it and convert it back to linked
    #list