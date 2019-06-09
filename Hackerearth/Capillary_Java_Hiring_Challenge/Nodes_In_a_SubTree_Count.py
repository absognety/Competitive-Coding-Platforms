'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import collections
L1 = [int(x) for x in input().split()]
N, Q = L1[0], L1[1]

treeValues = input()
graph = collections.defaultdict(list)
while(N-1 > 0):
    Input = input().split()
    graph[Input[0] + '-' + treeValues[int(Input[0])-1]].append(Input[1]+'-'+treeValues[int(Input[1])-1])
    N = N - 1

while(Q > 0):
    Input = input().split()
    C = 0
    if Input[0]+'-'+Input[1] in graph.keys():
        C += len(graph[Input[0]+'-'+Input[1]])
    if [Input[0]+'-'+Input[1]] in graph.values():
        for key,item in graph.items():
            if Input[0]+'-'+Input[1] in item:
                C += 1
    print (C)
    Q = Q - 1
