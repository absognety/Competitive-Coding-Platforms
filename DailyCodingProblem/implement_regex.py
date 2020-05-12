"""
Daily Coding Problem #25

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
    
That is, implement a function that takes in a string and a valid regular 
expression and returns whether or not the string matches the regular 
expression.

part - 1 :
    For example, given the regular expression "ra." and the string "ray", 
    your function should return true. The same regular expression on the 
    string "raymond" should return false.


part - 2:
    Given the regular expression ".*at" and the string "chat", your function 
    should return true. The same regular expression on the string "chats" 
    should return false.

"""

#part - 1 solution
def regex_match1(string,regex):
    v = regex.split('.')
    if v[0] != '':
        t = v[0]
    else:
        t = v[1]
    if (string.startswith(t) or string.endswith(t)):
        if len(string) == len(t) + 1:
            return 'true'
        return 'false'
    return 'false'        