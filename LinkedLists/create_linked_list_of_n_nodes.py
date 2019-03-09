from Creation_of_Linked_List import *

num_nodes = int(input())
arr = list(map(int,input().strip().split()))

if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(num_nodes):
        linkedList.insertNode(arr[i])
    linkedList.traversal()