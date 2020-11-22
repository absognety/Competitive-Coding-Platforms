#!/usr/bin/python3.8

"""
Daily Coding Problem #217

This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its 
binary representation. For example, 21 (10101) is sparse, but 22 
(10110) is not. For a given input N, find the smallest sparse number 
greater than or equal to N.

Do this in faster than O(N log N) time.

"""

def find_sparse_number(N):
    while True:
        binary_rep = bin(N)[2:]
        if binary_rep.count('1') == 1:
            return N
        c = binary_rep.find('1')
        if c == -1:
            pass
        else:
            checker = []
            s = c + 1
            for j in range(s,len(binary_rep)):
                if binary_rep[j] == '1':
                    if (j - c) == 1:
                        checker.append(False)
                        c = j
                    else:
                        checker.append(True)
                        c = j
            print (checker)
            if len(set(checker)) == 1:
                if True in checker:
                    return N
        N += 1
        
#Testcases for finding sparse numbers
print (find_sparse_number(19))
print (find_sparse_number(26))
print (find_sparse_number(39))