import itertools

def Sub_Sequences(STR):
    combs = []
    for l in range(1,len(STR)+1):
        combs.append(list(itertools.combinations(STR,l)))
    for c in combs:
        for t in c:
            print (''.join(t),end=' ')


if __name__ == '__main__':
    Sub_Sequences('geek')
    Sub_Sequences('geeks')
    Sub_Sequences('geeksforgeeks')
    Sub_Sequences('hackerrank')
    Sub_Sequences('hackerearth')
    Sub_Sequences('codechef')
