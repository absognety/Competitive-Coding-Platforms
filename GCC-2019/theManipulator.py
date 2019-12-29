"""
Given two encoded strings str1 and str2 consisting of upper-case 
English alphabets and the character ‘#’, decode the string based on the following operation:
Whenever a ‘#’ is encountered, increment the previously encountered 
alphabet by 1 (in a cyclic fashion i.e. A -> B, B -> C, ….., Z -> A). Finally, print Yes if both the strings are equal, else print No.
Note: Every string will begin with an English alphabet.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input containing str1 and str2 in separate lines.

Output:
For each testcase, in a new line, print Yes if the two strings 
become equal after the manipulation, else print No.

Constraints:
1 <= T <= 100
1 <= |str1, str2| <= 103

Examples:
Input:
2
E#R##C
FTA##
B
C
Output:
Yes
No

Explanation:
Testcase1: str1 = E#R##C, and str2 = FTA##. Now, in str1 we 
encounter # after E so we increment E to F. Next we encounter 
two # after R, so we increment R two times to T. So str1 becomes 
FTC. Similarly for str2 we encounter two # after A, so we increment 
A two times to C. str2 becomes FTC. Both strings are now equal so 
we print Yes.

"""

import string

def getCircular(a, n, ind):
    result = []
    i = ind 
    while i < n + ind : 
        result.append(a[(i % n)])
        i = i + 1
    return result

def transform_string(s):
    alphabets = string.ascii_uppercase
    res = ""
    l_s = len(s)
    nothashtag_inds_s1 = [i for i,j in enumerate(s) if j != '#']
    if l_s - nothashtag_inds_s1[-1] == 1:
        p = 0
        for q in range(1,len(nothashtag_inds_s1)):
            x = nothashtag_inds_s1[q] - nothashtag_inds_s1[p]
            n = x - 1
            char = s[nothashtag_inds_s1[p]]
            char_index = alphabets.index(char)
            all_chars = getCircular(alphabets,26,char_index)
            new_index = n
            res += all_chars[new_index]
            p += 1
        res += s[nothashtag_inds_s1[-1]]
    elif l_s - nothashtag_inds_s1[-1] > 1:
        p = 0
        for q in range(1,len(nothashtag_inds_s1)):
            x = nothashtag_inds_s1[q] - nothashtag_inds_s1[p]
            n = x - 1
            char = s[nothashtag_inds_s1[p]]
            char_index = alphabets.index(char)
            all_chars = getCircular(alphabets,26,char_index)
            new_index = n
            res += all_chars[new_index]
            p += 1
        n = l_s - nothashtag_inds_s1[-1] - 1
        char = s[nothashtag_inds_s1[-1]]
        char_index = alphabets.index(char)
        all_chars = getCircular(alphabets,l_s,char_index)
        new_index = n
        res += all_chars[new_index]
    return res

def manipulator(str1,str2):
    if ('#' not in str1) and ('#' not in str2):
        if str1 == str2:
            return "Yes"
        else:
            return "No"
    res1 = transform_string(str1)
    res2 = transform_string(str2)
    if res1 == res2:
        return "Yes"
    else:
        return "No"
                
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        s1 = input()
        s2 = input()
        print (manipulator(s1,s2))