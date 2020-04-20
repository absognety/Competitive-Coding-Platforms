"""
# Daily Coding Problem #3
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree 
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

# define a Node of tree
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# serialize the nodes of binary tree (tree => list)
def serialize(node:Node) -> list:
    serialized_result = []
    if node == None:
        return None
    stack = []
    stack.append(node)
    while (len(stack) != 0):
        h = stack.pop()
        if h != None:
            serialized_result.append(h.val)
            stack.append(h.right)
            stack.append(h.left)
        else:
            serialized_result.append("#")
    return serialized_result

# deserialize the nodes of binary tree (list => tree)
def deserialize(data:list):
    if len(data) == 0:
        return None
    t = [0]
    return helper(data,t)

def helper(arr,t):
    if (arr[t[0]] == "#"):
        return None
    root = Node(arr[t[0]])
    t[0] += 1
    root.left = helper(arr,t)
    t[0] += 1
    root.right = helper(arr,t)
    return root

# Testcases
node = Node('root',Node('left',Node('left.left')),Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

res = serialize(root)
org = deserialize(res)