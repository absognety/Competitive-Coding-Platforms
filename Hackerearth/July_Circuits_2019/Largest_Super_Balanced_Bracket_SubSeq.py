####### Super Balanced Bracket ########

#####Super Balanced Bracket Sub sequence with largest length#####
##### Contiguous sub-sequences are considered here #####
import queue
def isBalanced(seq):
    myqueue = queue.LifoQueue(maxsize=len(seq))
    for i in seq:
        if i == '(':
            myqueue.put(i)
        if myqueue.empty():
            return False
        if i == ')':
            x = myqueue.get()
            if x != '(':
                return False
    return (myqueue.empty())

def LargestSuperBalancedSubSeq(seq):
    isbalanced = isBalanced(seq)
    if isbalanced:
        maxSuperBalancedSubSeqLens = set()
        i = 1
        mylist = []
        while i <= len(seq):
            for j in range(len(seq)):
                myseq = seq[j:j+i]
                if myseq not in mylist:
                    mylist.append(myseq)
                    if isBalanced(myseq):
                        if (('(' in set(myseq[:len(myseq)//2])) & (')' not in set(myseq[:len(myseq)//2]))) & ((')' in set(myseq[len(myseq)//2:])) & ('(' not in set(myseq[len(myseq)//2:]))):
                               maxSuperBalancedSubSeqLens.add(len(myseq))
            i += 1
    return max(maxSuperBalancedSubSeqLens)
                            
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        seq = input()
        print (LargestSuperBalancedSubSeq(seq))