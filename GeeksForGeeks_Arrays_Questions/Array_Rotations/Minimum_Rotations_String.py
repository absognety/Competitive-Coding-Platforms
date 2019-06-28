def min_rotations(s):
    char = s[0]
    t = s[1:] + char
    c = 1
    while (s!=t and len(s)==len(t)):
        char = t[0]
        t = t[1:] + char
        c += 1
    return (c)


if __name__ == '__main__':
    S = input()
    print (min_rotations(S)) 