"""
Daily Coding Problem #212

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: 
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, 
given 1, return "A". Given 27, return "AA".

"""
import itertools
import string
import math

home = string.ascii_uppercase

def alphabetical_cid(mystring,n):
    p = math.log(n,26)
    if math.floor(p) == p == 0:
        x = 1
    elif p == math.floor(p):
        x = math.floor(p)
        y = math.floor(p) - 1
    else:
        x = math.floor(p) + 1
        y = math.floor(p)
    permutations = list(set(itertools.product(mystring,repeat=x)))
    print ("Number of permutations with repetition: ",len(permutations))
    permutations = sorted(["".join(y) for y in permutations])
    print ("printing the sample: ",permutations[:10])
    if math.floor(p) == p == 0:
        return permutations[n-1]
    if x == math.floor(p) + 1:
        diff = abs(n - pow(26,y))
        return permutations[diff-1]
    elif x == math.floor(p):
        return permutations[n-1]

print (alphabetical_cid(home,1))
print (alphabetical_cid(home,27))
print (alphabetical_cid(home,13244))
print (alphabetical_cid(home,15888))
print (alphabetical_cid(home,456976))
print (alphabetical_cid(home,377828))
print (alphabetical_cid(home,220387))