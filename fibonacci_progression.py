def fibonacciSeries(a,b,n):
    i=0
    while (i<=n):
        c = a+b
        a=b
        b=c
        print (c)
        i+=1
        
N = int(input())
a,b=1,1
fibonacciSeries(a,b,N)