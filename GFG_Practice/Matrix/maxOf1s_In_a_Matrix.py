import re
def maxNumOf1s(R,C,entries):
    matrix = []
    numof1s=[]
    for i in range(0,len(entries),C):
        matrix.append(entries[i:i+C])
    for m in matrix:
        y = ''.join(str(i) for i in m)
        numof1s.append(len(re.findall('1',y)))
    max1s = max(numof1s)
    return (numof1s.index(max1s))


if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        R,C = list(map(int,input().strip().split()))
        entries = list(map(int,input().strip().split()))
        print (maxNumOf1s(R,C,entries))