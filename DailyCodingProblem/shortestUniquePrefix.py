"""
Daily Coding Problem #162

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of 
each word. For example, given the list:

dog
cat
apple
apricot
fish

Return the list:

d
c
app
apr
f

"""

def longestCommonPrefix(a): 
      
    size = len(a) 
  
    # if size is 0, return empty string  
    if (size == 0): 
        return "" 
  
    if (size == 1): 
        return a[0] 
  
    # sort the array of strings  
    a.sort() 
      
    # find the minimum length from  
    # first and last string  
    end = min(len(a[0]), len(a[size - 1])) 
  
    # find the common prefix between  
    # the first and last string  
    i = 0
    while (i < end and 
           a[0][i] == a[size - 1][i]): 
        i += 1
  
    pre = a[0][0: i] 
    return pre 

def shortest_unique_prefix(arr_words):
    base = arr_words[0]
    prefixes = []
    for n in range(1,len(arr_words)):
        select_arr = [base,arr_words[n]]
        common_prefix = longestCommonPrefix(select_arr)
        
        if common_prefix:
            if base == common_prefix:
                prefixes.append(base)
            else:
                prefixes.append(common_prefix + base[len(common_prefix)])
            
            if arr_words[n] == common_prefix:
                prefixes.append(arr_words[n])
            else:
                prefixes.append(common_prefix + arr_words[n][len(common_prefix)])
        
        else:
            prefixes.append(base[0])
            prefixes.append(arr_words[n][0])
        base = arr_words[n]
    prefixes = list(set(prefixes))
    if len(prefixes) > len(arr_words):
        result = prefixes.copy()
        l = 0
        remove_elements = []
        while (l <= len(result)-1):
            ele = prefixes.pop(l)
            checker = ["T" if ele in px else "F" for px in prefixes]
            if "T" in checker:
                remove_elements.append(ele)
            prefixes.insert(l,ele)
            l += 1
        for e in remove_elements:
            result.remove(e)
        return result
    else:
        return prefixes
    
if __name__ == '__main__':
    for tc in range(int(input())):
        arr_words = input().strip().split(" ")
        print (shortest_unique_prefix(arr_words))