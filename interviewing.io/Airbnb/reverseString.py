"""
Write a quick function that reverses a given string

"""


#Index based method
def reverse_string(s):
    return s[::-1]

#Using built-in reverse method on class list
def reverse_string1(s):
    h = list(s)
    h.reverse()
    return "".join(h)


#Using O(n) auxiliary space
def reverse_string2(s):
    v = len(s)
    u = [''] * v
    for c in range(v):
        u[v-c-1] = s[c]
    return ''.join(u)

#Two pointer approach to swap the characters
#Use O(n) space as strings are immutable
def reverse_string3(s):
    start = 0
    end = len(s) - 1
    s = list(s)
    while (start != end):
        temp = s[start]
        s[start]=s[end]
        s[end] = temp
        start += 1
        end -= 1
    return "".join(s)
        

if __name__ == '__main__':
    string = "competitive"
    print (reverse_string(string))
    print (reverse_string1(string))
    print (reverse_string2(string))
    print (reverse_string3(string))