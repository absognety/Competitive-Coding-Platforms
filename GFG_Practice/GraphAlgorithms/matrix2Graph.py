"""
1. Edges between cells that share an edge
2. Traversal is only possible horizontally and vertically
"""

import collections
def matrix2graph(mlist):
    ihor=0
    iver=0
    G=collections.defaultdict(list)
    for ihor in range(len(mlist)):
        for iver in range(len(mlist[0])):
            if ihor==0 and iver==0:
                G['a'+str(ihor)+str(iver)] = [mlist[ihor][iver+1],mlist[ihor+1][iver]]
                
            elif ihor==0 and iver==len(mlist[0])-1:
                G['a'+str(ihor)+str(iver)] = [mlist[ihor][iver-1],mlist[ihor+1][iver]]
                
            elif ihor==len(mlist)-1 and iver==0:
                G['a'+str(ihor)+str(iver)] = [mlist[ihor-1][iver],mlist[ihor][iver+1]]
                
            elif ihor==len(mlist)-1 and iver==len(mlist[0])-1:
                G['a'+str(ihor)+str(iver)] = [mlist[ihor][iver-1],mlist[ihor-1][iver]]
                
            elif (0 < ihor < len(mlist)-1) and (iver==0):
                G['a'+str(ihor)+str(iver)] = [mlist[ihor-1][iver],mlist[ihor][iver+1],mlist[ihor+1][iver]]
                
            elif (0 < ihor < len(mlist)-1) and (iver==len(mlist[0])-1):
                G['a'+str(ihor)+str(iver)] = [mlist[ihor-1][iver],mlist[ihor][iver-1],mlist[ihor+1][iver]]
                
            elif (ihor==0) and (0 < iver < len(mlist[0])-1):
                G['a'+str(ihor)+str(iver)] = [mlist[ihor][iver-1],mlist[ihor][iver+1],mlist[ihor+1][iver]]
                
            elif (ihor==len(mlist)-1) and (0 < iver < len(mlist[0])-1):
                G['a'+str(ihor)+str(iver)] = [mlist[ihor-1][iver],mlist[ihor][iver-1],mlist[ihor][iver+1]]
                
            elif (0 < ihor < len(mlist)-1) and (0 < iver < len(mlist[0])-1):
                G['a'+str(ihor)+str(iver)] = [mlist[ihor-1][iver],mlist[ihor][iver-1],mlist[ihor][iver+1],mlist[ihor+1][iver]]
                
    return (G)
            
                    
if __name__ == '__main__':
    N = int(input())
    matrix_list = []
    for i in range(N):
        arr = list(map(int,input().strip().split()))
        matrix_list.append(arr)
    print (matrix2graph(matrix_list))