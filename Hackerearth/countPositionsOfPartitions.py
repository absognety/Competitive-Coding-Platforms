import collections

def countPositions(S,K):
    partitions=[]
    for i in range(len(S)-1):
        partitions.append((S[:i+1],S[i+1:]))
    C=0
    for x in partitions:
        first = collections.Counter(x[0])
        second = collections.Counter(x[1])
        firstKeys = first.keys()
        secondKeys = second.keys()
        commonKeys = set(firstKeys).intersection(set(secondKeys))
        if len(commonKeys) >= K:
            P = {a:first[a] for a in commonKeys}
            Q = {b:second[b] for b in commonKeys}
            if P==Q:
                C+=1
    return (C)
    
if __name__ == '__main__':
    K = int(input())
    S = input()
    print (countPositions(S,K))