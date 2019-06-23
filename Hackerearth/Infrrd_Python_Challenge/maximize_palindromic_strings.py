import collections
def maxPalindStrings(s,p):
    cls1 = collections.Counter(p)
    cls2 = collections.Counter(s)
    sumcls1 = sum(cls1.values())
    sumcls2 = sum([q for p,q in cls2.items() if p in cls1])
    if sumcls2%sumcls1 == 0:
        return (sumcls2//sumcls1)
    else:
        return (int(sumcls2/sumcls1))
    
if __name__ == '__main__':
    sl,pl = list(map(int,input().strip().split()))
    s = input()
    p = input()
    print (maxPalindStrings(s,p))