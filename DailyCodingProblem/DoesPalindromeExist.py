"""
Daily Coding Problem #157

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is 
a palindrome.

For example, carrace should return true, since it can be 
rearranged to form racecar, which is a palindrome. daily 
should return false, since there's no rearrangement that can 
form a palindrome.

"""

import itertools
def checkPalindrome(word):
    l = len(word)
    for w in itertools.permutations(word,l):
        w = "".join(w)
        if w == w[::-1]:
            return 'true'
    return 'false'

print (checkPalindrome('carrace'))
print (checkPalindrome('daily'))