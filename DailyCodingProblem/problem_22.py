"""

Daily Coding Problem #22

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
['bedbath', 'and', 'beyond'].

"""
import re
import operator
def unique_by_key(elements, key=None):
    if key is None:
        key = lambda e: e
    return {key(el): el for el in elements}.values()

def construction(string,words):
    result = []
    ismissing = []
    for word in words:
        if re.search(word,string):
            result.append((word,re.search(word,string).span()[0]))
        else:
            ismissing.append(1)
    if ismissing:
        return 'null'
    result = unique_by_key(result,key=operator.itemgetter(1))
    result = sorted(result,key=lambda x: x[1])
    result = [d[0] for d in result]
    return result

if __name__ == '__main__':
    words = {'quick','brown','the','fox'}
    string = 'thequickbrownfox'
    print (construction(string,words))
    
    words2 = {'bed','bath','bedbath','and','beyond'}
    string2 = 'bedbathandbeyond'
    print (construction(string2,words2))