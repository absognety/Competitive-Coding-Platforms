'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
 
def colorful_ways(n,k):
    a = k
    b = (k-1)**(n-1)
    return (a*b)
 
if __name__=='__main__':
    T = int(input())
    for tcase in range(T):
        N,K = list(map(int,input().strip().split()))
        print (colorful_ways(N,K)%((10**9) + 7))