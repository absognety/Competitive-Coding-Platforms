def printNto1(n):
    if n < 1:
        return
    else:
        print (n)
        printNto1(n-1)