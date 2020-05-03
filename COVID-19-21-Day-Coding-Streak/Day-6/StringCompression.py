"""
You are given a large number of strings which you have to compress. 
If the process of compressing them is correctly done, the original 
string can be retreived by decompressing the compressed string. The 
process of decompressing is shown below :
    1. Lets say the compressed string is ab*c*x
    2. Iterate over the string from left to right, if you find a '*', 
    remove it, and simply add a duplicate of the string on the left. 
    Do this process repeatedly till all stars are removed.
    
    ex: Decompressing : ab*c*d -> ababc*d -> ababcababcd

Your task is to compress string to its smallest possible form. In case 
there are multiple ways to compress a string, prefer the one which return 
smaller output. For example, if input is zzzzzzz, output should be z*z*z 
and not z**zzz

Input: First line of input contains number of test cases T. Then T test 
cases follow. Each test case contains the string to be shortened in a 
newline. Input string consists solely of small case letters. Input will 
be read by driver code.

Output: The shortened string is to be printed as output. Output will be 
printed by driver code.

Your task: Your task is to complete the function compress() which takes 
the input string as argument and returns the compressed string.

Constraints: T <= 500 ; 1 <= |s| <= 105

Example:
Input:
2
ababcababcd
zzzzzzz
Output:
ab*c*d
z*z*z

"""