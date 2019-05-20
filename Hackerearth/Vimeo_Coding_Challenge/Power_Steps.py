"""
A bunglow consist of  rooms numbered from 1 to N. Two rooms u and v are having door between them if only and if their difference is power of 3. But there is no door if their difference is 0th power of 3.

The amount of time taken(in minutes) to open a door is equal to a, where 3^a is equal to the difference between rooms that are connected via that door. i.e the door between room 1 and room 10 will take 2 minutes to open as the difference is 9 which is 2 power of 3.

You are given T testcases. In every testcase three integers N,u and v are given. You are supposed to find the minimum time require to move from v to u.

You can move only in either strictly increasing or stricly decreasing manner. Every testcase is independent of other test cases.

Input

First line consists of one integer T, the number of testcases. T lines follow.

Every line consists of three integers N, u and v denoting the number of rooms.

Constraints

1 <= T <= 10^5
1 <= N <= 10^18
1 <= u,v <= N

Output

You are supposed to print minimum time to meet them. If they can't meet print -1(without quotes).

Print answer for each testcase in new line.


"""
import math
def Solution (arr,n):
    # Write your code here
    N = arr[0]
    d1,d2 = min(arr[1],arr[2]),max(arr[1],arr[2])
    if str(math.log(d2-d1,3)).split('.')[1] == '0' and str(math.log(d2-d1,3)).split('.')[0] != '0':
        return (int(math.log(d2-d1,3)))
    else:
        reqMediators = []
        for x in range(d1+1,d2):
            if (str(math.log(x-d1,3)).split('.')[1]=='0' & str(math.log(x-d1,3)).split('.')[0]!='0') & (str(math.log(d2-x,3)).split('.')[1]=='0' & str(math.log(d2-x,3)).split('.')[0]!='0'):
                reqMediators.append(x)
        if reqMediators:
            allTimes = []
            for y in reqMediators:
                allTimes.append(int(math.log(y-d1,3)) + int(math.log(d2-y,3)))
            return (min(allTimes))
        else:
            return (-1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int,input().strip().split()))
        print (Solution(arr,t))