class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None
class Tree:
    def createNode(self,data):
        return (Node(data))
    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if ch == 'L':
            node.left = self.insert(node.left,data,ch)
            return (node.left)
        else:
            node.right = self.insert(node.right,data,ch)
            return (node.right)
    
    def search(self,lis,data):
        for i in lis:
            if i.data == data:
                return (i)
        
def printLeftView(root):
    result = [root.data]
    while (root.left is not None):
        result.append(root.left.data)
        root = root.left
    print (' '.join(str(i) for i in result))
    
    
#Driver Program
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = input().strip().split()
        if n==0:
            print('')
            continue
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root,int(arr[0]),'L')
        lis.append(root)
        k=0
        for J in range(n):
            ptr = None
            ptr = tree.search(lis,int(arr[k]))
            lis.append(tree.insert(ptr,int(arr[k+1]),arr[k+2]))
            k+=3
        printLeftView(root)
        print('')
