class Stack():
    def __init__(self):
        self.stack=[]
        self.max_val=None
        self.length=0
        
    def push(self,val):
        self.length+=1
        if val>self.max_val or max_val is None:
            self.stack.append(2*val+max_val)
            self.max_val=val
        self.stack.append(val)
        
    def pop(self):
        if self.length ==0:
            return None
        else:
            top=self.stack.pop()
            if top=self.max_val:
                self.max_val=  
            return top
        
    def max(self):
        if self.max_val:
            return self.max_val
        else:
            return None


if __name__=='__main__':
    s=Stack()
    s.push(89)
    s.push(80)
    s.push(90)
    s.max()
    s.pop()
    s.max()
