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

import re
def regex_match1(string,regex):
    #part - 1 solution
    if (('*' not in regex) and ('.' in regex)):
        if len(string) != len(regex):
            return 'false'
        indices_period = []
        for ind,val in enumerate(regex):
            if val == '.':
                indices_period.append(ind)
        collector = [[]]
        for m in range(len(string)):
            if m not in indices_period:
                collector[-1].append(m)
            else:
                collector.append([])
        tracker = []
        for lis in collector:
            if lis != []:
                for q in lis:
                    if regex[q] == string[q]:
                        tracker.append(True)
                    else:
                        return 'false'
        assert len(set(tracker)) == 1,"some of characters are mismatching"
        return 'true'
    elif ('*' in regex):
        #part - 2 solution
        re_match = re.search(regex,string)
        c = re_match.span()
        if len(string) != len(string[c[0]:c[1]]):
            return 'false'
        return 'true'