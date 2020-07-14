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


#this handles only distinct values in array
def find_pairs(arr,x):
    value_dict = {}
    for value in arr:
        value_dict[value] = True
    for value in arr:
        target_compliment = x - value
        if target_compliment in value_dict:
            return ("{} and {}".format(target_compliment,value))
    return ("No valid pairs")


def find_pairs2(arr,x):
    value_dict = {}
    for value in arr:
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 0
    for value in arr:
        target_compliment = x - value
        if target_compliment in value_dict:
            if target_compliment == value:
                if not value_dict[target_compliment] > 0:
                    continue
            return "{} and {}".format(target_compliment,value)
    return "No valid pairs"


if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        arr = list(map(int,input().strip().split()))
        x = int(input())
        print (find_pair(arr, x))   
        print (find_pairs(arr, x))
        print (find_pairs2(arr, x))