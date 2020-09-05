"""
Daily Coding Problem #143

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into 
three parts.

The first part contains all elements in lst that are less 
than x
The second part contains all elements in lst that are 
equal to x
The third part contains all elements in lst that are 
larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and 
lst = [9, 12, 3, 5, 14, 10, 10], one partition may be 
[9, 3, 5, 10, 10, 12, 14].

"""

def partition_list(lst,x):
    first = []
    second = []
    third = []
    for u in lst:
        if u < x:
            first.append(u)
        elif u == x:
            second.append(u)
        else:
            third.append(u)
    return (first + second + third)


if __name__ == '__main__':
    for tc in range(int(input())):
        lst = list(map(int,input().strip().split()))
        x = int(input())
        print (partition_list(lst, x))