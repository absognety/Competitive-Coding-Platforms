"""
Given an array arr of size n containing only distinct integers, you need to find total times you see a series of consecutive integers of length greater than 1.
A series of consecutive integers is defined as arr[i], arr[i]+1, arr[i]+2...and so on.

Input:
The first line of input contains T denoting the numbers of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains the size of array n. The second line contains the elements of the array.

Output:
For each testcase, in a newline, print the total times you see a series of consecutive numbers.

Constraints:
1 <= T <= 100
1 <= n <= 103
0 <= arri <= 107

Examples:
Input:
3
7
5 7 9 10 11 13 14
6
0 1 2 4 5 7
7
1 0 2 9 3 8 6
Output:
2
2
0

Explanation:
Testcase1: The array is {5 7 9 10 11 13 14}. Here, 9 10 11 is one series of 
consecutive integers with length greater than 1. Again, 13 14 is another 
series of consecutive integers with length greater than 1. So, a total of two 
times we see such a series. Hence the answer is 2.

"""

def continuousSeries(arr,n):
    req=[]
    el = 0
    for i in range(1,n):
        if arr[i] - arr[el] == 1:
            if len(req) == 0:
                req.append([arr[el],arr[i]])
                el += 1
                
            else:
                req[-1].extend([arr[el],arr[i]])
                el += 1
        else:
            if len(req) != 0:
                req.append([])
            el += 1
            continue
    if len(req) == 0:
        return 0
    elif len(req) > 0:
        ans = [i for i in req if len(i) > 0]
        return len(ans)
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (continuousSeries(arr,n))