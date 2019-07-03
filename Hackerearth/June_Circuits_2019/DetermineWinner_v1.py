import itertools
import math
def find_winner(n,k):
    players = ['A','D']
    winnersList = []
    for i in range(1,k+1):
        a = n/i
        if str(a).split('.')[1] == 0: 
            gturns = list(itertools.islice(itertools.cycle(players),a+1))
            winnersList.append(gturns[len(gturns)-1])
        else:
            gturns = list(itertools.islice(itertools.cycle(players),math.ceil(a)+1))
            winnersList.append(gturns[len(gturns)-1])
    if len(set(winnersList))==1:
        if winnersList[0]=='A':
            return ('Dishant')
        else:
            return ('Arpa')
    else:
        if winnersList[len(winnersList)-1] == 'D':
            return ('Dishant')
        else:
            return ('Arpa')
            
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n,k = list(map(int,input().strip().split()))
        print (find_winner(n,k))