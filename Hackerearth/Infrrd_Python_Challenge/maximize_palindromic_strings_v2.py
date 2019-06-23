import re
import itertools
if __name__ == '__main__':
    sl,pl = list(map(int,input().strip().split()))
    s = input()
    p = input()
    x = [len(re.findall(p,''.join(i))) for i in list(itertools.permutations(s,len(s)))]
    print (max(x))
    
#### Memory Limit exceeded #### 
### Exhaustive solution ####