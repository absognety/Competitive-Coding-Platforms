"""
Minimize the number of replacements to get a string with 
same number of ‘a’, ‘b’ and ‘c’ in it

Given a string consisting of only three possible characters ‘a’, ‘b’ or ‘c’. 
The task is to replace characters of the given string with ‘a’, ‘b’ or ‘c’ 
only such that there are equal number of characters of ‘a’, ‘b’ and ‘c’ in 
the string. The task is to minimize the number of replacements and print 
the lexicographically smallest string possible of all such strings with the 
minimal replacements.

If it is not possible to obtain such a string, print -1.

Examples:

Input : s = "bcabba"
Output : bcabca
Number of replacements done is 1 and this is
the lexicographically smallest possible 

Input : "aaaaaa"
Output : aabbcc

Input : "aaaaa"
Output : -1


Approach:

1. Count the number of ‘a’, ‘b’ and ‘c’ in the string.
2. If the count of them is equal then the same string will be the answer.
3. If length of the string is not a multiple of 3, then it is not possible.
4. First, reduce the number of exceeding a’s in the string.
   a. Replace ‘c’ by ‘a’ if there are extra ‘c’ using a sliding window technique from left.
   b. Replace ‘b’ by ‘a’ if there are extra ‘b’ using a sliding window technique from left in case of no ‘c’ at an index.
5. Secondly, reduce the number of exceeding b’s in the string by replacing ‘c’ from front using sliding window.
6. Thirdly, reduce the number of exceeding c’s by reducing the number of extra ‘a’ from the back using sliding window.
7. Fourthly, reduce the number of exceeding b’s in the string by reducing the number of extra ‘a’ from the back.
8. Fifthly, reduce the number of exceeding c’s if any by reducing the number of extra ‘b’ from the back.


We keep on replacing from back in order to get lexicographically smallest string.

"""
def minimize_replacements(STR):
    #Count of a's, b's and c's in a given string
    count_a = STR.count('a')
    count_b = STR.count('b')
    count_c = STR.count('c')
    # if three of them are equal return the same string
    if count_a == count_b == count_c:
        return (STR)
    
    #if not a multiple of 3 then return -1
    if len(STR)%3 != 0:
        return -1
    #Increase the number of a's by 
    #removing extra 'b' and ;c;
    i=0
    s = list(STR)
    while ((count_a < len(STR)//3) & (i < len(STR))):
        #Check if it is 'b' and it more than n/3
        if ((STR[i]=='b') & (count_b > len(STR)//3)):
            count_b-=1
            s[i]='a'
            count_a+=1
        #Check if it is 'c' and it more than n/3 
        elif ((STR[i]=='c') & (count_c > len(STR)//3)):
            count_c-=1
            s[i]='a'
            count_a+=1
        i+=1
    
    
    i=0
    STR = ''.join(s)
    t = list(STR)
    #Increase the number of b's by removing extra 'c' 
    while ((count_b < len(STR)//3) & (i < len(STR))):
        #Check if it is 'c' and it more than n/3 
        if ((STR[i] == 'c') & (count_c > len(STR)//3)):
            count_c-=1 
            t[i]='b'
            count_b+=1
        i+=1
    
    
    i = len(STR) - 1
    STR = ''.join(t)
    u = list(STR)
    #Increase the number of c's from back 
    while ((count_c < len(STR)//3) & (i >= 0)):
        #Check if it is 'a' and it more than n/3 
        if ((STR[i] == 'a') & (count_a > len(STR)//3)):
            count_a-=1
            u[i] = 'c'; 
            count_c+=1 
        i-=1
        
    
    
    i = len(STR) - 1 
    STR = ''.join(u)
    v = list(STR)
    #Increase the number of b's from back 
    while ((count_b < len(STR)//3) & (i >= 0)):
        #Check if it is 'a' and it more than n/3 
        if ((STR[i] == 'a') & (count_a > len(STR)//3)):
            count_a-=1 
            v[i] = 'b' 
            count_b+=1
        i-=1
        
        
    
    i = len(STR) - 1
    STR = ''.join(v)
    w = list(STR)
    #Increase the number of c's from back 
    while ((count_c < len(STR)//3) & (i >= 0)):
        #Check if it is 'b' and it more than n/3 
        if ((STR[i] == 'b') & (count_b > len(STR)//3)):
            count_b-=1
            w[i] = 'c'
            count_c+=1
        i-=1
        
        
    STR = ''.join(w)
    return STR
    

if __name__ == '__main__':
    print (minimize_replacements('bcabba'))
    print (minimize_replacements('aaaaaa'))
    print (minimize_replacements('aabcbabbc'))
    print (minimize_replacements('aaabcbcbc'))
    print (minimize_replacements('aaaaa'))
    