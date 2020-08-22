"""
Daily Coding Problem #125

This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two 
nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.

"""
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None
  
def insert(root,data): 
    if root is None: 
        return Node(data) 
    if(data < root.data): 
        root.left = insert(root.left, data) 
    if(data > root.data): 
        root.right = insert(root.right, data) 
    return root 


def findPairUtil(root, summ, unsorted_set,result): 
    if root is None: 
        return False
    if findPairUtil(root.left,summ,unsorted_set,result): 
        return True
    if unsorted_set and (summ-root.data) in unsorted_set: 
        result.append((summ-root.data,root.data))
        return True
    else: 
        unsorted_set.add(root.data) 
  
    return findPairUtil(root.right,summ, unsorted_set,result) 

def findPair(root,summ): 
    unsorted_set = set() 
    result = []
    res = findPairUtil(root,summ,unsorted_set,result)
    if(res): 
        print("Pair exists and it is {}".format(result)) 
    else:
        print ("Pair does not exist!!")
  
# Driver code 
if __name__=='__main__': 
    root=None
    root = insert(root,15) 
    root = insert(root,10) 
    root = insert(root,20) 
    root = insert(root,8) 
    root = insert(root,12) 
    root = insert(root,16) 
    root = insert(root,25) 
    root = insert(root,10) 
    summ = 33
    findPair(root, summ) 
    
    root=None
    root = insert(root,10) 
    root = insert(root,5) 
    root = insert(root,15) 
    root = insert(root,11) 
    root = insert(root,15) 
    summ = 20
    findPair(root,summ)