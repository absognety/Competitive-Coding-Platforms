class Stack():
    
    def __init__(self,sequence):
        
        self._seq = sequence
        self._length = len(sequence)
        self.top=len(sequence)-1
        
    def push(self,X):
        if (self.top==self._length-1):
            print ('Stack Overflow Condition')
        else:
            self._seq.append('')
            self.top+=1
            self._seq[self.top]=X
    
    def pop(self):
        if (self.top==-1):
            print ('Stack is empty, Underflow Condition!!')
        else:
            self._seq.pop(self.top)
            self.top-=1
    
    def topElement(self):
        return self._seq[self.top]
    
    def size(self):
        return (self.top+1)
