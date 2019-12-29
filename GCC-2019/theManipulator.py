import string

def getCircular(a, n, ind):
    result = []
    i = ind 
    while i < n + ind : 
        result.append(a[(i % n)])
        i = i + 1
    return result

def transform_string(s):
    alphabets = string.ascii_uppercase
    res = ""
    l_s = len(s)
    nothashtag_inds_s1 = [i for i,j in enumerate(s) if j != '#']
    if l_s - nothashtag_inds_s1[-1] == 1:
        p = 0
        for q in range(1,len(nothashtag_inds_s1)):
            x = nothashtag_inds_s1[q] - nothashtag_inds_s1[p]
            n = x - 1
            char = s[nothashtag_inds_s1[p]]
            char_index = alphabets.index(char)
            all_chars = getCircular(alphabets,26,char_index)
            new_index = n
            res += all_chars[new_index]
            p += 1
        res += s[nothashtag_inds_s1[-1]]
    elif l_s - nothashtag_inds_s1[-1] > 1:
        p = 0
        for q in range(1,len(nothashtag_inds_s1)):
            x = nothashtag_inds_s1[q] - nothashtag_inds_s1[p]
            n = x - 1
            char = s[nothashtag_inds_s1[p]]
            char_index = alphabets.index(char)
            all_chars = getCircular(alphabets,26,char_index)
            new_index = n
            res += all_chars[new_index]
            p += 1
        n = l_s - nothashtag_inds_s1[-1] - 1
        char = s[nothashtag_inds_s1[-1]]
        char_index = alphabets.index(char)
        all_chars = getCircular(alphabets,l_s,char_index)
        new_index = n
        res += all_chars[new_index]
    return res

def manipulator(str1,str2):
    if ('#' not in str1) and ('#' not in str2):
        if str1 == str2:
            return "Yes"
        else:
            return "No"
    res1 = transform_string(str1)
    res2 = transform_string(str2)
    if res1 == res2:
        return "Yes"
    else:
        return "No"
                
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        s1 = input()
        s2 = input()
        print (manipulator(s1,s2))