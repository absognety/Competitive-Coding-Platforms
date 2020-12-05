"""
Find the Inorder Successor of a given key in BST

In Binary Tree, Inorder successor of a node is the next 
node in Inorder traversal of the Binary Tree. Inorder 
Successor is NULL for the last node in Inorder traversal. 
In Binary Search Tree, Inorder Successor of an input node 
can also be defined as the node with the smallest key 
greater than the key of the input node. So, it is sometimes 
important to find next node in sorted order.

"""

class Node: 
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key 
        

def find_inorder_successor(root,number):
    successors = []
    def inorder_traversal(root,num):
        if root:
            inorder_traversal(root.left,num)
            if root.val > num:
                successors.append(root.val)
            inorder_traversal(root.right, num)
    inorder_traversal(root, number)
    return min(successors)


if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    print (find_inorder_successor(root,3))
    root = Node(20)
    root.left = Node(9)
    root.right = Node(25)
    root.left.left = Node(5)
    root.left.right = Node(12)
    root.left.right.left = Node(11)
    root.left.right.right = Node(14)
    print (find_inorder_successor(root, 9))
    print (find_inorder_successor(root, 14))