def fibonacciSeries(a,b,n):
    i=0
    fib = [a,b]
    while (i<=n):
        c = a+b
        a=b
        b=c
        fib.append(c)
        print (c)
        i+=1
    return (fib)
        
N = int(input())
a,b=1,1
fibonacciSeries(a,b,N)