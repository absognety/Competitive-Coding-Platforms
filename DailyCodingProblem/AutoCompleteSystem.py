"""
Daily Coding Problem #11
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set 
of all possible query strings, return all strings in the set that have s 
as a prefix.

For example, given the query string de and the set of strings 
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data 
structure to speed up queries.

"""

def auto_complete(s,stringset):
    return [x for x in stringset if x.startswith(s)]

if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        s = input()
        stringset = input().strip().split()
        print (auto_complete(s,stringset))