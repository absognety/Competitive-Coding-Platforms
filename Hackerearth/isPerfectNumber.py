'''
Write a function that decides whether a given number is perfect number or not

Definition:
    A perfect number is a number whose sum of divisors except for number itself
    is equal to itself (proper divisors)
    
    Ex: 6 = 1 + 2 + 3 (6 is a perfect number)
        5 != 1 (5 is not a perfect number)
        14 = 1 + 2 + 7 (Not a perfect number)
        28 = 1 + 2 + 4 + 7 + 14 (28 is a perfect number)
'''

# Write your code here
def is_perfect_number(n):
    total = 1
    i = 2
    while (i*i <= n):
        if (n%i) == 0:
            if (i*i != n):
                total += (i + n//i)
            else:
                total += i
        i += 1
    if (total == n) and (n != 1):
        return 1
    else:
        return 0

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        if is_perfect_number(N):
            print ("YES")
        else:
            print ("NO")