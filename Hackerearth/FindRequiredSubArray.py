"""

You are given an array A of N elements. You need to find all the subarrays such that their average sum is greater than the average sum of the remaining array elements. You need to print the start and end index of each subarray in sorted order in a new line.
Notes: 

A subarray which starts at  position L1 and ends at position R1 comes before a subarray that starts at L2 and ends at R2 if L1<L2 or if L1=L2 but R1<=R2
The array indexes are in the range 1 to N.
The average sum of an empty array is 0.
Input
The first line contains an integer N that denotes the total number of elements in the array.
The next line contains N space separated integers that denote the elements of the array  .

Output
The first line of output should contain an integer X that denotes how many subarrays that follow the given criterion are there.
The next X lines contain a pair of space-separated integers corresponding to the start and end positions of the valid subarrays.

Constraints

1 <= N <= 2000
1 <= A[i] <= 10**6

"""

def findMaxAverageSumSubArray(arr):
    allSubArrays = []
    for step in range(1,len(arr)+1):
        for i in range(0,len(arr)):
            allSubArrays.append(arr[i:i+step])
    distinctSubArrays = []
    for x in allSubArrays:
        if x not in distinctSubArrays:
            distinctSubArrays.append(x)
    h = 1
    answerArrays=[]
    while (h <= len(arr)):
        array = [i for i in distinctSubArrays if len(i)==h]
        avgSumArray = [sum(i)/len(i) for i in array]
        maxAvgSum = max(avgSumArray)
        answerArrays.append(array[avgSumArray.index(maxAvgSum)])
        h += 1
    print (len(answerArrays))
    result=[]
    for y in answerArrays:
        v = len(y)
        if v == 1:
            result.append(' '.join((str(arr.index(y[0])+1),str(arr.index(y[0])+1))))
        else:
            result.append(' '.join((str(arr.index(y[0])+1),str(arr.index(y[v-1])+1))))
    for x in sorted(result):
        print (x)
    print (answerArrays,allSubArrays,distinctSubArrays)
    
if __name__== '__main__':
    N = int(input())
    arr = list(map(int,input().strip().split()))
    findMaxAverageSumSubArray(arr)