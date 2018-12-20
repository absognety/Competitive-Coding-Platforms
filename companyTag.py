#  Change a Company Tag using algorithms #

print (
   """
   There is a Company with a Tag comment (string) that when we divide the 
   comment into equal sub strings - All are supposed to be equal
   
   However we have incorrect Tags assigned to the company which we need
   to change.
   
   The Task is:
       
   for a given Tag comment we need to check that all the sub-strings are equal
   
   if not, we need to change the sub-strings so that all will be same
   in such a way that the cost of doing this operation is minimum
   
   The cost of changing a to b is 1 which is difference between the 
   locations of a and b in alphabets
   
   Example:     Given string -> aabaaabab, K = 3,
                            aab | aaa | bab
                            The cost is equal to a->b + b->a i.e 1+1 = 2
                            result : aab | aab | aab (All are equal)
                            
   """)

import string
import numpy as np
STRG = input()
k = int(input())

alphabs = list(string.ascii_lowercase)
costs = [alphabs.index(i)+1 for i in alphabs]
CHARS = len(alphabs)

def correction_strg(strg,K):
    if (len(strg)%K == 0):
        sub_lists = []
        for i in range(0,len(strg),K):
            sub_lists.append(strg[i:i+K])
        
        if (len(list(set(sub_lists)))!=1):
            uniq_lists = list(set(sub_lists))
            costArr=[]
            for s in uniq_lists:
                costArr.append([alphabs.index(i) for i in s])
        
            costArr = np.array(costArr)
            
            diff=[]
            for I in range(len(costArr)):
                sum_diff=0
                for J in range(len(costArr)):
                    if (I!=J):
                        w = (I,J)
                        q = abs(np.subtract(costArr[I],costArr[J])).sum()
                        sum_diff+=q
                diff.append(sum_diff)
                        
            return (diff,costArr,sub_lists,w)        
    else:
        print ('Unequal Partitions')
        return


x = correction_strg(STRG,k)
print (min(x[0]))
