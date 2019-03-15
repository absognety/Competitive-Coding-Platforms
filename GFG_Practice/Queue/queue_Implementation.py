class Queue():
    
    def __init__(self,sequence):
        self._seq = sequence
        self._length = len(sequence)
        self.front = 0
        self.rear = len(sequence)-1
        
    def enqueue(self,X):
        if (self.rear>=self._length-1):
            print ("Queue Overflow")
            
        else:
            self._seq.append('')
            self.rear+=1
            self._seq[self.rear]=X
             
    def dequeue(self):
        if (len(self._seq)==0):
            print ('Queue is empty, No entity to dequeue')
            
        else:
            self._seq.pop(self.front)
            self.rear-=1
            
    def get_front(self):
        return (self.front)
    
    def get_rear(self):
        return (self.rear)
    
    def get_size(self):
        return (self.rear-self.front+1)
    
    def get_queue(self):
        return (self._seq)
    