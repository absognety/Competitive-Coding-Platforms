'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

You are given a range [L,R] . You are required to find the number of integers  
in the range such that GCD(X,F(X)) > 1 where F(X) is equal to the sum of 
digits of X in its hexadecimal (or base 16) representation.

For example, F(27) = 1 + B = 1 + 11 = 12 
( 27 in hexadecimal is written as 1B). You are asked T such questions. 

Input format

The first line contains a positive integer T denoting the number of questions 
that you are asked.
Each of the next T lines contain two integers L and R denoting the range of 
questions.

'''
# Hexadecimal synopsis - transformations
lookup_dict = {"A":10,"B":11,"C":12,
              "D":13,"E":14,"F":15}

def gcd(a,b):
    if b == 0:
        return a 
    else:
        return gcd(b,a%b)

def convert_hex_to_int(hex_rep):
    elements = list(hex_rep)
    result = 0
    N = len(elements)
    i = 1
    j = 0
    while (N-i >= 0):
        if elements[j] in lookup_dict:
            result += (pow(16,N-i) * lookup_dict[elements[j]])
        else:
            result += (int(elements[j]) * pow(16,N-i))
        i += 1
        j += 1
    return result


def hexadecimal_numbers(L,R):
    C = 0
    for n in range(L,R+1):
        hex_rep = hex(n)[2:].upper()
        Fx = convert_hex_to_int(hex_rep)
        if gcd(n,Fx) > 1:
            C += 1
    return C

T = int(input())
while (T > 0):
    L,R = list(map(int,input().strip().split()))
    print (hexadecimal_numbers(L,R))
    T -= 1