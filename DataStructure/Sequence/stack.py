class Stack:
    def __init__(self,size = 20):
        self.items = [None]*size
        self.numItems = 0
        self.size = size

    def top(self):
        if self.numItems !=0 :
            return self.items[self.numItems -1]
        raise IndexError("Stack is empty")

    def push(self, item):
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1
    
    def allocate(self):
        newlength = self.size *2
        newStack = [None]*newlength
        for i in range(self.numItems):
            newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength

    def pop(self):
        if self.numItems == self.size//4:
            self.deallocate()
        if self.numItems != 0:
            topelement = self.items[self.numItems -1]
            self.numItems -=1
            return topelement
        raise IndexError("Stack is empty")

    def deallocate(self):
        newlength = self.size //2
        newStack = [None]*newlength
        for i in range(self.numItems):
           newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength

    def is_empty(self):
        if self.numItems !=0:
            return False
        return True



stack = Stack(size = 10)
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())