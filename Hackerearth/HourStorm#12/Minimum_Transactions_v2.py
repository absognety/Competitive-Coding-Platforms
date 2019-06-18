def mainf():
    s = input().split();
    n,m = int(s[0]),int(s[1]);
    d = {};
    while(m>0):
        tran = input().split();
        d[tran[0]] = d[tran[0]] + int(tran[2])*(-1) if tran[0] in d.keys() else int(tran[2])*(-1);
        d[tran[1]] = d[tran[1]] + int(tran[2]) if tran[1] in d.keys() else int(tran[2]);
        m-=1;
    sum = 0;
    for v in d.values():
        sum+=v if v>0 else 0
    print(sum);
	
mainf();