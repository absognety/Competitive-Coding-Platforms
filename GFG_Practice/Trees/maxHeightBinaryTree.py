"""
question from GeeksforGeeks

Given a binary tree, find height of it. Height of empty tree is 0 and 
height of below tree is 2. 
 
Example Tree

Recursively calculate height of left and right subtrees of a node 
and assign height to the node as max of the heights of two children 
plus 1. See below pseudo code and program for details.
Algorithm: 
 
maxDepth()
1. If tree is empty then return 0
2. Else
     (a) Get the max depth of left subtree recursively  i.e., 
          call maxDepth( tree->left-subtree)
     (b) Get the max depth of right subtree recursively  i.e., 
          call maxDepth( tree->right-subtree)
     (c) Get the max of max depths of left and right 
          subtrees and add 1 to it for the current node.
         max_depth = max(max dept of left subtree,  
                             max depth of right subtree) 
                             + 1
     (d) Return max_depth
See the below diagram for more clarity about execution of the recursive function maxDepth() for above example tree. 
 

            maxDepth('1') = max(maxDepth('2'), maxDepth('3')) + 1
                               = 1 + 1
                                  /    \
                                /         \
                              /             \
                            /                 \
                          /                     \
               maxDepth('2') = 1                maxDepth('3') = 0
= max(maxDepth('4'), maxDepth('5')) + 1
= 1 + 0   = 1         
                   /    \
                 /        \
               /            \
             /                \
           /                    \
 maxDepth('4') = 0     maxDepth('5') = 0

"""


#/usr/bin/python3.9
from PIL import Image
import os
image_path = os.path.dirname(__file__)
print (image_path)

#Display the tree for this question
img = Image.open(os.path.join(image_path,"tree122.gif"))
img.show()

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
        
class BinaryTree:
    def __init__(self,root):
        self.root = root
    def maxDepth(self,node):
        if node == None:
            return -1
        else:
            ldepth = self.maxDepth(node.left)
            rdepth = self.maxDepth(node.right)
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
            
            
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    tree = BinaryTree(root)
    print (tree.maxDepth(root))