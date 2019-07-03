def find_winner(n,k):
    if n%(k+1)==0:
        return ('Dishant')
    else:
        return ('Arpa')
            
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n,k = list(map(int,input().strip().split()))
        print (find_winner(n,k))