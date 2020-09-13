"""
Daily Coding Problem #147

Given a list, sort it using this method: reverse(lst, i, j), 
which reverses lst from i to j.

"""

def reverse(lst,i,j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

temp = 0
def sort_list(arr):
    for m in range(len(arr)):
        for p in range(m+1,len(arr)):
            if arr[m] > arr[p]:
                arr = reverse(arr,m,p)
    return arr

if __name__ == '__main__':
    T = int(input())
    while (T > 0):
        arr = list(map(int,input().strip().split()))
        print (sort_list(arr))
        T -= 1