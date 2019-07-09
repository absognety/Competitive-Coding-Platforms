def balanced_partition(points,persons):
    total_pe = sum(persons)
    h = {}
    for i in range(len(points)):
        h[points[i][0]-points[i][1]] = h.get(points[i][0]-points[i][1],0) + persons[i]
    avg = total_pe / 2
    t = 0
    for key in sorted(h.keys()):
        t += h[key]
        if t >= avg:
            if t > avg:
                if total_pe == 2*t - h[key]:
                    return ("YES")
                else:
                    return ("NO")
            else:
                return ("YES")
            break
        
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        persons = []
        for l in range(n):
            p,q,m = list(map(int,input().strip().split()))
            points.append([p,q])
            persons.append(m)
        print (balanced_partition(points,persons))