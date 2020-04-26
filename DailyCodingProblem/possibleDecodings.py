"""
Daily Coding Problem #7
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count 
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded 
as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not 
allowed.

"""
import string
import itertools
letters = string.ascii_lowercase
nums = list(range(1,27))
mapping = dict(zip(nums,letters))

def findCombinationsUtil(arr,index,num,reducedNum):
    global combinations
    if reducedNum < 0:
        return
    
    #If combination is  
    #found, print it
    if reducedNum == 0:
        combinations.append([])
        for i in range(0,index):
            combinations[-1].append(arr[i])
        #print()
        return
    prev = 1 if index==0 else arr[index-1]
    for k in range(prev,num+1):
        arr[index] = k
        findCombinationsUtil(arr, index + 1, num, reducedNum - k)

# Function to find out all  
# combinations of positive  
# numbers that add upto given 
# number. It uses findCombinationsUtil()
        
def findCombinations(n):
    #array to store the combinations 
    #It can contain max n elements 
    arr = [0]*n
    
    #find all combinations 
    findCombinationsUtil(arr, 0, n, n)
    return combinations

def decode_message(msg):
    if '0' in msg:
        return "invalid message" 
    n = len(msg)
    all_decoded = findCombinations(n)
    possible_decodings = []
    for c in all_decoded:
        possible_perms = set(itertools.permutations(c,len(c)))
        for pp in possible_perms:
            tracker = []
            letters = []
            f = 0
            g = 0
            while (f < sum(pp)):
                if int(msg[f:f+pp[g]]) > 26:
                    tracker.append(0)
                    break
                tracker.append(1)
                letters.append(mapping.get(int(msg[f:f+pp[g]])))
                f += pp[g]
                g += 1
            if 0 not in tracker:
                possible_decodings.append(letters)
    return possible_decodings

if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        msg = str(input())
        combinations = []
        print (decode_message(msg))