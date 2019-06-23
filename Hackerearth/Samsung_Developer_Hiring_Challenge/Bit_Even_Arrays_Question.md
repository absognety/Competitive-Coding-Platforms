There is an array A of size N with entries as integers, some of the entries are -1. we need to replace -1's with numbers satisfying below criteria.
The binary representation of number to be replaced with should have only 0's in its odd positions and the number has to be even.
The array entries A[i] with which you replace -1's with are in such a way that A[i]>=A[i-1] and also for given array A[0]!=-1
Find the minimum sum of array entries possible after the above operations are done.

Input format:
```
First line T - number of test cases
second line N - size of array
Third line - N space separated integers
```

Sample Input:
```
1
8
1 5 -1 25 -1 7 35 -1
```

Sample Output:
`153`

Explanation:
```
Index 2: Replacing -1 with 8 as its binary representation is 1000 which has 0 in its odd places and 8 is even and 8 >=5
Index 4: Replacing -1 with 32 as its binary representation is 100000 which has 0 in its odd places and 32 is even and 32>=25
Index 7: Replacing -1 with 40 as its binary representation is 101000 which has 0 in its odd places and 40 is even and 40>=35
```
