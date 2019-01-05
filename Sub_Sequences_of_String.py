strg = input()

import itertools
combs = []
for l in range(1,len(strg)+1):
    combs.append(list(itertools.combinations(strg,l)))
    
for c in combs:
    for t in c:
        print (''.join(t),end=' ')
