"""
Daily Coding Problem #211

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all 
occurrences of the pattern in the string. For example, given the string 
"abracadabra" and the pattern "abr", you should return [0, 7].

"""

import re
def find_pattern(pattern,string):
    indices = []
    for m in re.finditer(pattern,string):
        indices.append(m.span()[0])
    return indices

if __name__ == '__main__':
    pattern = "abr"
    string = "abracadabra"
    print (find_pattern(pattern,string))
    pattern = "eee"
    string = "bsbsnsnnsqeiieee@$ghhg88888****eeednjdjskan!!!!^%&"
    print (find_pattern(pattern,string))