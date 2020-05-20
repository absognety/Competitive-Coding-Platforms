"""
Daily Coding Problem #27

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return 
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

Algorithm:
    1. Declare a character stack S.
    2. Now traverse the expression string exp.
    3. If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack. 
    4. If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the 
    matching starting bracket then fine else parenthesis are not balanced.
    5. After complete traversal, if there is some starting bracket left in stack 
    then “not balanced”

"""

def isParenthesExprBalanced(string):
    stack = []
    for c in string:
        if c in ['{','(','[']:
            stack.append(c)
        else:
            # IF current character is not opening  
            # bracket, then it must be closing.   
            # So stack cannot be empty at this point.  
            if len(stack) == 0:
                return False
            current = stack.pop()
            if current == '(':
                if c != ')':
                    return False
            if current == '{':
                if c != '}':
                    return False
            if current == '[':
                if c != ']':
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
    expr1 = "[()]{}{[()()]()}"
    expr2 = "[(])"
    
    if isParenthesExprBalanced(expr): 
        print("Balanced")  
    else : 
        print("Not Balanced")
        
    if isParenthesExprBalanced(expr1): 
        print("Balanced")  
    else : 
        print("Not Balanced")
        
    if isParenthesExprBalanced(expr2): 
        print("Balanced")  
    else : 
        print("Not Balanced")