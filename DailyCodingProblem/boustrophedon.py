"""
Daily Coding Problem #258

This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to 
right, the second line going right to left, and continuing to go back and forth. 
This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon 
order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].

"""

#class for new Node in a tree
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    #Base case
    if root == None:
        return
    # Create an empty queue for level order tarversal  
    q = []
    #Enqueue Root and initialize height
    q.append(root)
    level_position = 1
    while (len(q) != 0):
        # nodeCount (queue size) indicates number 
        # of nodes at current lelvel.
        nodeCount = len(q)
        # Dequeue all nodes of current level and  
        # Enqueue all nodes of next level 
        level = []
        while (nodeCount > 0):
            node = q[0]
            level.append(node.data)
            q.pop(0)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
            nodeCount -= 1
        #print from left to right when level is at 1,3,5,7......
        if level_position%2 != 0:
            for e in level:
                print (e,end=" ")
        #print from right to left when level is at 2,4,6,8.....
        else:
            for e in range(len(level)-1,-1,-1):
                print (level[e],end= " ")
        #incrementing the level_position by 1
        level_position += 1
        print ()
    return


if __name__ == '__main__':
    # Let us create binary tree shown above  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    printLevelOrder(root)