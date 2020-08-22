"""
Daily Coding Problem #123

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the 
different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"

"""

def is_string_number(s):
    if s.isdigit():
        return True
    exc = None
    try:
        g = float(s)
    except Exception as e:
        exc = e
        pass
    if exc is None:
        if (g < 0) or (g > 0):
            return True
    else:
        return False
        
    
if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        s = input()
        print (is_string_number(s))