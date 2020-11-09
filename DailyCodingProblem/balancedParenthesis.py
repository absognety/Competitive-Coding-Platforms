"""
Daily Coding Problem #199

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be 
produced from it using the minimum number of insertions and deletions. 
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you 
could return "()()()()".

"""

from IsStringBalanced import isParenthesExprBalanced

def findBalancedString(string):
    if len(string) == 0:
        return string
    if isParenthesExprBalanced(string):
        return string
    parenthesis_map = {')':'(','}':'{',']':'['}
    reverse_parenthesis_map = {b:a for a,b in parenthesis_map.items()}
    #print (reverse_parenthesis_map)
    open_parenthesis = ['{','(','[']
    counter = 0
    res = []
    for c in string:
        if c in open_parenthesis:
            res.append(c)
            counter += 1
        else:
            if counter == 0:
                res.append(parenthesis_map[c])
            else:
                counter -= 1
            res.append(reverse_parenthesis_map[parenthesis_map[c]])
    while (counter > 0):
        if c in open_parenthesis:
            res.append(reverse_parenthesis_map[c])
        else:
            res.append(c)
        counter -= 1
    return res

print (findBalancedString("(()"))
print (findBalancedString("))()("))
print (findBalancedString("}{{"))
#Appropriate solution for same type of braces
print (findBalancedString("{[)]{"))