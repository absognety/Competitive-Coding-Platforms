import collections

def maxDrawRounds(s1,s2,n):
    assert len(s1)==n,"string length msimatch"
    assert len(s2)==n,"string length msimatch"
    s1_counter = collections.Counter(s1)
    s2_counter = collections.Counter(s2)
    common_keys = set(s1_counter.keys()) & set(s2_counter.keys())
    ind_list = []
    for k in common_keys:
        ind_list.append(s1_counter[k]==s2_counter[k])
    sum_value = 0
    sum1=0
    sum2=0
    if len(common_keys)==0:
        return (0)
    if len(set(ind_list))==1 and list(set(ind_list))[0]==True:
        for k in common_keys:
            sum_value += s1_counter[k] #s2_counter or s1_counter
        return (sum_value)
    else:
        for k in common_keys:
            sum1 += s1_counter[k]
            sum2 += s2_counter[k]
        return (min(sum1,sum2))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        nrounds = int(input())
        string1 = input()
        string2 = input()
        print (maxDrawRounds(string1,string2,nrounds))