n = int(input())
def sumOfDigits(n):
    if n < 10:
        return n
    else:
        return (sumOfDigits(n//10) + n%10)
    
print (sumOfDigits(253))
print (sumOfDigits(9987))