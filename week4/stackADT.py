class Stack:
    
    def __init__(self):
        self.top = -1
        self.items= []
        
    def is_empty(self):
        return (self.top == -1);

    def push(self,newItem):
        self.top+=1
        self.items.append(newItem);

    def pop(self):
        if (self.is_empty()):
            return None
        else:
            self.top-=1
            return self.items.pop()

    def peek(self):
        if (self.is_empty()):
            return None
        else:
            return self.items[self.top]

    def size(self):
        return len(self.items)
    
    # Trying the max method with O(n) solution
    def max_method(self) -> int:
        """
        Input: Stack
        Output: Integer
        """
        if self.is_empty():
            return None
        return max(self.items) # O(n) where it iterates through the stack. 
    
    
        

if __name__=="__main__": # only runs this part when the file is the main file
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.max_method())
	
