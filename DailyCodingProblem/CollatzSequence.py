"""
Daily Coding Problem #210

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting 
with any positive integer:
    1. if n is even, the next number in the sequence is n / 2
    2. if n is odd, the next number in the sequence is 3n + 1
    3. It is conjectured that every such sequence eventually reaches 
    the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""

def collatz_sequence(n):
    count = 0
    while True:
        if n==1:
            count += 1
            break
        if n%2 == 0:
            count += 1
            print (n//2,end=" ")
            n = n//2
        else:
            count += 1
            print (3*n + 1,end=" ")
            n = (3*n) + 1
    print ("\nlength of the sequence: ", count)
    print ("\n")

#Testing for various entries of n
collatz_sequence(68)
collatz_sequence(287)
collatz_sequence(29928)
collatz_sequence(1000000)
collatz_sequence(999999)
collatz_sequence(999997)
collatz_sequence(1818288278)

#999999 will be the input that gives the longest sequence