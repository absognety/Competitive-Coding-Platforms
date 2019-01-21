'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N, M = list(map(int,input().strip().split()))

arr = list(map(int,input().strip().split()))

if M in arr:
    inds = []
    for i in range(len(arr)):
        if (arr[i] == M):
            inds.append(i+1)
    print (max(inds))
else:
    print (-1)
            

