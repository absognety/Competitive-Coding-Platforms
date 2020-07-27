"""
Daily Coding Problem #103

Given a string and a set of characters, return the shortest substring 
containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters 
{a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, 
return null.

"""

chars = {'a','e','i'}
def getShortestSubstring(s):
    length = len(s)
    alist = [] 
    for i in range(length):
        for j in range(i,length):
            if chars.issubset(s[i:j+1]):
                alist.append(s[i:j+1])
    if not alist:
        return "null"
    result = alist[0]
    for sbs in alist[1:]:
        if len(sbs) < len(result):
            result = sbs
    return result


if __name__ == '__main__':
    T = int(input())
    while (T > 0):
        s = input()
        print (getShortestSubstring(s))
        T -= 1