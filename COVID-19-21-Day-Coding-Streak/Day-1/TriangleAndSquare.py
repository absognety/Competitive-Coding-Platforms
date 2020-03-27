def triangleAndSquare(base):
    if base <= 2:
        return 0
    else:
        if base%2 == 0:
            base = base - 2
            base = base / 2
            return int((base * (base + 1)/2))
        else:
            base = base - 1
            base = base - 2
            base = base / 2
            return int((base * (base + 1)/2))
    
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        b = int(input())
        print (triangleAndSquare(b))