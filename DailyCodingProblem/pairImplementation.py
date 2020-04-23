"""

# Daily Coding problem #5

Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
first and last element of that pair. For example, car(cons(3, 4)) 
returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr

"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def parse_pair(a,b):
    return (a,b)

def car(pair):
    return pair(parse_pair)[0]

def cdr(pair):
    return pair(parse_pair)[1]

if __name__ == '__main__':
    a = 3
    b = 4
    upair = cons(a,b)
    print (car(upair))
    print (cdr(upair))