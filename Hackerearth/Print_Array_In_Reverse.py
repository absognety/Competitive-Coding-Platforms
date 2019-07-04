'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
if __name__=='__main__':
    
    N = int(input())
    xarr=[]
    for H in range(N):
        x = int(input())
        xarr.append(x)
        
    for k in xarr[::-1]:
        print (k)