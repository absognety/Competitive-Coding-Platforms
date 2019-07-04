"""
Given a string str, the task is to print all the sub-sequences of str.
A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining 
elements.

Examples:

Input: str = “abc”
Output: a b ab c ac bc abc

Input: str = “geek”
Output: g e ge e ge ee gee k gk ek gek ek gek eek geek


Approach: 

Write a recursive function that prints every sub-sequence of the 
sub-string starting from the second character str[1, n – 1] after appending 
the first character of the string str[0] in the beginning of every sub-sequence. 
Terminating condition will be when the passed string is empty, 
in that case the function will return an empty arraylist.

"""


import itertools

def Sub_Sequences(STR):
    combs = []
    for l in range(1,len(STR)+1):
        combs.append(list(itertools.combinations(STR,l)))
    for c in combs:
        for t in c:
            print (''.join(t),end=' ')


if __name__ == '__main__':
    Sub_Sequences('geek')
    Sub_Sequences('geeks')
    Sub_Sequences('geeksforgeeks')
    Sub_Sequences('hackerrank')
    Sub_Sequences('hackerearth')
    Sub_Sequences('codechef')
