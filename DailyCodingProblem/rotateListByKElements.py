"""
Daily Coding problem #126

This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, 
[1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. How many swap 
or move operations do you need?

"""

def rotateList(arr,k):
    return (arr[k:] + arr[:k])

if __name__ == '__main__':
    for tcase in range(int(input())):
        arr = list(map(int,input().strip().split()))
        k = int(input())
        print (rotateList(arr, k))