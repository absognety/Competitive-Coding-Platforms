from queue_Implementation import Queue

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N,K = list(map(int,input().strip().split()))
        seq = list(map(int,input().strip().split()))
        myQueue = Queue(seq)
        givenList = myQueue._seq[:K]
        otherList = myQueue._seq[K:]
        for v in range(len(seq)):
            myQueue.dequeue()
        for u in givenList[::-1]:
            myQueue.enqueue(u)
        print (myQueue._seq + otherList)