"""
Daily Coding Problem #188

This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?

"""


def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

## Output
#3
#3
#3
## Explanation:
#   when loop gets completed i is saved as 3 globally, so when we
#   initialized make_functions to a variable, all functions should
#   return 3

#Alter function to print what we want -> 1, 2, 3
def make_functions():
    flist = []
    for i in [1, 2, 3]:
        def print_i():
            return (i)
        flist.append(print_i())

    return flist

functions = make_functions()
for f in functions:
    print (f)