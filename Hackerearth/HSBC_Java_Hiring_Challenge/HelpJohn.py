def helpJohn(arr):
    bag = []
    xlen = len(arr)
    i = 0
    while (xlen > 0):
        a = arr[i]
        if len(bag)==0:
            print (' '.join(['-1','-1']))
        else:
            lessArr = [i for i in bag if i < a]
            q1a = max(lessArr) if lessArr else -1
            moreArr = [i for i in bag if i > a]
            q2a = min(moreArr) if moreArr else -1
            print (' '.join([str(q1a),str(q2a)]))
        bag.append(a)
        i += 1
        xlen -= 1
        

if __name__ == '__main__':
    N = int(input())
    xint = []
    for n in range(N):
        Int = int(input())
        xint.append(Int)
    helpJohn(xint)