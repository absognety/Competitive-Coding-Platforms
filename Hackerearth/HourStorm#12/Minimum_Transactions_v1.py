import collections
def minTransact(trans_arr,n):
    ai = set([i[0] for i in trans_arr])
    bi = set([i[1] for i in trans_arr])
    if ai == bi:
        trans_dict = collections.defaultdict(list)
        for a in trans_arr:
            trans_dict[tuple(a[:2])].append(a[2])
        assert len(trans_dict.keys())<=2,"Something Went Wrong"
        arr_sum = [sum(val) for key,val in trans_dict.items()]
        if len(arr_sum) > 1:
            return (abs(arr_sum[0] - arr_sum[1]))
        else:
            return (arr_sum[0])
    else:
        wing_dict = collections.defaultdict(list)
        for a in trans_arr:
            wing_dict[a[0]].append(a.index(a[0]))
            wing_dict[a[1]].append(a.index(a[1]))
        bways_items = []
        for b,val in wing_dict.items():
            if len(set(val)) > 1:
                bways_items.append(b)
        trans_amount_bways = collections.defaultdict(list)
        for w in bways_items:
            for z in trans_arr:
                if w in z[:2]:
                    trans_amount_bways[w].append(z[2])
        temp_sum = set([u[0] if len(set(u))==1 else max(u) for k,u in trans_amount_bways.items()])
        trans = set([s[2] for s in trans_arr])
        last_ent = trans.difference(temp_sum)
        return (sum(temp_sum) + sum(last_ent))
                
if __name__ == '__main__':
    n,m = list(map(int,input().strip().split()))
    trans_arr = []
    for line in range(m):
        arr = list(map(int,input().strip().split()))
        trans_arr.append(arr)
    print (minTransact(trans_arr,n))