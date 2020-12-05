"""
Daily Coding Problem #231

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no 
two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", 
return None.

"""
from heapq import heappop,heappush
import heapq
import string
from queue import PriorityQueue
from collections import Counter
import functools


@functools.total_ordering
class Key(object):
    def __init__(self,val:int,c:str):
        self.freq = val
        self.ch = c
    
    def __gt__(self,other):
        return (self.freq > other.freq)
        
    def __lt__(self,other):
        return (self.freq < other.freq)
        
    def __eq__(self,other):
        return (self.freq == other.freq)
        
    
def rearrange_characters(strg):
    letters = string.ascii_lowercase
    MAX_CHAR = 26
    count = [0] * MAX_CHAR
    n = len(strg)
    for i in range(n):
        count[ord(strg[i]) - ord('a')] += 1
    print (count)
        
    pq = PriorityQueue()
    for c in letters:
        val = ord(c) - ord('a')
        if count[val] > 0:
            pq.put(Key(count[val],c))
            
    result = ""
    prev = Key(-1,"#")
    while (pq.qsize() > 0):
        k = pq.get()
        result += k.ch
        if prev.freq > 0:
            pq.put(prev)
        k.freq -= 1
        prev = k
        
    print (result)
    
    if n != len(result):
        return "Not a Valid string"
    else:
        return result
    
    
def reorganizeString(S: str) -> str:
    counter = Counter(S)
   
    # if one element is more than half, no answer
    if any(freq > (len(S) + 1) // 2 for freq in counter.values()):
       return "Not a Valid String"
   
    # max-heap
    pq = [(-freq, ch) for ch, freq in counter.items()]
    heapq.heapify(pq)
   
    # get two elements at once and concat
    res = []
    while len(pq) >= 2:
        cnt1, ch1 = heappop(pq)
        cnt2, ch2 = heappop(pq)
        res.append(ch1 + ch2)
       
        if cnt1 + 1:
            heappush(pq, (cnt1 + 1, ch1))
       
        if cnt2 + 1:
            heappush(pq, (cnt2 + 1, ch2))
    print (res)
    print (pq)
   
    return ''.join(res) if not pq else ''.join(res) + pq[0][1]
    
    
if __name__ == '__main__':
    print (rearrange_characters("aaabbc"))
    print (rearrange_characters("aaab"))
    
    print (reorganizeString("aaabbc"))
    print (reorganizeString("aaabc"))
    print (reorganizeString("aaab"))