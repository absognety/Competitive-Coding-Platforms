class Stack():
    
    def __init__(self,sequence):
        
        self._seq = list(sequence)
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
    
    def get_stack(self):
        return (self._seq)

if __name__ == '__main__':
    stack1 = Stack([3,9,4,2,0,-3,65,72,1])
    stack1.push(23)
    stack1.pop()
    stack1.pop()
    print (stack1.topElement())
    print (stack1.size())
    print (stack1.get_stack())
    stack1.push(45)
    print (stack1.get_stack())
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.push(100)
    stack1.push(283)
    stack1.push(136)
    print (stack1.get_stack())