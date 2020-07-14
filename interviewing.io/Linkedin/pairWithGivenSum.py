"""
Given a list of whole positive numbers, How would you go about finding two 
numbers that sum up to a given target number
"""

def find_pair(arr,x):
    start = 0
    end = len(arr)-1
    arr = sorted(arr)
    while (start < end):
        if arr[start] + arr[end] == x:
            print ("found it")
            return (arr[start],arr[end])
        elif arr[start] + arr[end] > x:
            end -= 1
            print ("decrementing end")
        elif arr[start] + arr[end] < x:
            start += 1
            print ("incrementing start")
    return -1

if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        arr = list(map(int,input().strip().split()))
        x = int(input())
        print (find_pair(arr, x))      