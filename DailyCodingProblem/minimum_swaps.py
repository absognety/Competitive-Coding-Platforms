"""
Daily Coding Problem #240

This problem was asked by Spotify.

There are N couples sitting in a row of length 2 * N. They are currently 
ordered randomly, but would like to rearrange themselves so that each 
couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?

Solution copied from Geeksforgeeks

"""

# Python program to find 
# minimum number of swaps 
# required so that 
# all pairs become adjacent. 

# This function updates 
# indexes of elements 'a' and 'b' 
def updateindex(index,a,ai,b,bi): 

	index[a] = ai 
	index[b] = bi 


# This function returns minimum 
# number of swaps required to arrange 
# all elements of arr[i..n] 
# become aranged 
def minSwapsUtil(arr,pairs,index,i,n): 

	# If all pairs procesed so 
	# no swapping needed return 0
    if (i > n):
        return 0

	# If current pair is valid so 
	# DO NOT DISTURB this pair 
	# and move ahead.
    if (pairs[arr[i]] == arr[i+1]):
        return minSwapsUtil(arr, pairs, index, i+2, n) 

	# If we reach here, then arr[i] 
	# and arr[i+1] don't form a pair 

	# Swap pair of arr[i] with 
	# arr[i+1] and recursively compute 
	# minimum swap required 
	# if this move is made.
    one = arr[i+1]
    indextwo = i+1
    indexone = index[pairs[arr[i]]]
    two = arr[index[pairs[arr[i]]]] 
    arr[i+1],arr[indexone]=arr[indexone],arr[i+1] 
    updateindex(index, one, indexone, two, indextwo) 
    
    a = minSwapsUtil(arr, pairs, index, i+2, n) 

	# Backtrack to previous configuration. 
	# Also restore the 
	# previous indices, 
	# of one and two 

    arr[i+1],arr[indexone]=arr[indexone],arr[i+1] 
    updateindex(index, one, indextwo, two, indexone) 
    one = arr[i] 
    indexone = index[pairs[arr[i+1]]] 

	# Now swap arr[i] with pair 
	# of arr[i+1] and recursively 
	# compute minimum swaps 
	# required for the subproblem 
	# after this move 
    two = arr[index[pairs[arr[i+1]]]] 
    indextwo = i 
    arr[i],arr[indexone]=arr[indexone],arr[i] 
    updateindex(index, one, indexone, two, indextwo) 
    b = minSwapsUtil(arr, pairs, index, i+2, n) 

	# Backtrack to previous 
	# configuration. Also restore 
	# 3 the previous indices, 
	# of one and two 
    arr[i],arr[indexone]=arr[indexone],arr[i] 
    updateindex(index, one, indextwo, two, indexone) 

	# Return minimum of two cases 
    return 1 + min(a, b) 

# Returns minimum swaps required 
def minSwaps(n,pairs,arr): 

    index=[] # To store indices of array elements 
    for i in range(2*n+1+1):
        index.append(0) 

	# Store index of each 
	# element in array index 
    for i in range(1,2*n+1):
        index[arr[i]] = i 

	# Call the recursive function 
    return minSwapsUtil(arr, pairs, index, 1, 2*n) 

# Driver code 

# For simplicity, it is 
# assumed that arr[0] is 
# not used. The elements 
# from index 1 to n are 
# only valid elements 
arr = [0, 3, 5, 6, 4, 1, 2] 

# if (a, b) is pair than 
# we have assigned elements 
# in array such that 
# pairs[a] = b and pairs[b] = a 
pairs= [0, 3, 6, 1, 5, 4, 2] 
m = len(pairs) 

n = m//2 # Number of pairs n 
		# is half of total elements 

# If there are n 
# elements in array, then 
# there are n pairs 
print("Min swaps required is ",minSwaps(n, pairs, arr)) 