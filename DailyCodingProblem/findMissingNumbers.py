"""
Daily Coding Problem #390

This problem was asked by Two Sigma.

You are given an unsorted list of 999,000 unique integers, each from 1 
and 1,000,000. Find the missing 1000 numbers. What is the computational 
and space complexity of your solution?

"""

def missing_numbers(full_list,given_list):
    return set(full_list)-set(given_list)

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        full_list = range(1,1000001)
        given_list = range(5,999005)
        print (missing_numbers(full_list, given_list))