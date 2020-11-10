"""
Daily Coding Problem #202

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a 
palindrome. Do not convert the integer into a string.

"""

def isIntegerPalindrome(num):
    if len(str(num)) == 0:
        return "empty string"
    if len(str(num)) == 1 and str(num).isdigit():
        return True
    digits = []
    if (num%10) == 0:
        return False
    while (num%10 != 0):
        digits.append(num%10)
        num = num//10
    if digits == digits[::-1]:
        return True
    return False

print (isIntegerPalindrome(888))
print (isIntegerPalindrome(121))
print (isIntegerPalindrome(678))
print (isIntegerPalindrome(234432))
print (isIntegerPalindrome(23))
print (isIntegerPalindrome(""))
print (isIntegerPalindrome(8))