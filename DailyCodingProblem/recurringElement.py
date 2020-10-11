"""
Daily Coding Problem #159

This problem was asked by Google.

Given a string, return the first recurring character in it, 
or null if there is no recurring character.

For example, given the string "acbbac", return "b". 
Given the string "abcdef", return null.

"""

import collections
import random
def find_recurring_element(string):
    all_recurring_elements = []
    for c in string:
        if string.count(c) > 1:
            all_recurring_elements.append(c)
    if all_recurring_elements:
        return random.choice(all_recurring_elements)
    return 'null'

def recurring_element(string):
    all_recurring_elements = []
    mydict = collections.Counter(string)
    for k,v in mydict.items():
        if v > 1:
            all_recurring_elements.append(k)
    if all_recurring_elements:
        return random.choice(all_recurring_elements)
    return "null"

print (recurring_element('acbbac'))
print (recurring_element("abcdef"))
print ()
print (find_recurring_element("acbbac"))
print (find_recurring_element("abcdef"))