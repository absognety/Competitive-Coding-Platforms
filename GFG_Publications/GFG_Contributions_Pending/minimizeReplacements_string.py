"""
Minimize the number of replacements to get a string with 
same number of ‘a’, ‘b’ and ‘c’ in it
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
    