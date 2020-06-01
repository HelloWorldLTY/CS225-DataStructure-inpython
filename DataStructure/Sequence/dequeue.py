
class Fifo:
    def __init__(self,size=20):
        self.items = [None] * size
        self.first = 0
        self.last = -1
        self.size = size
        self.length = 0
    def isEmpty(self):
        if self.length != 0:
            return False
        return True
    def front(self):
        if self.length != 0:
            return self.items[self.first]
        raise ValueError("Queue is empty")
    def back(self):
        if self.length != 0:
            return self.items[self.last]
        raise ValueError("Queue is empty")
    def pushback(self,item):
        if self.length == self.size:
            self.allocate()
        self.last = (self.last + 1) % self.size
        self.items[self.last] = item
        self.length += 1
    def popfront(self):
        if self.size > 20 and self.length == self.size / 4:
            self.deallocate()
        if self.length != 0:
            frontelement = self.items[self.first]
            self.first = (self.first + 1) % self.size
            self.length -= 1
            return frontelement
        raise ValueError("Queue is empty")
    def allocate(self):
        newlength = 2 * self.size
        length = self.length
        newQueue = [None] * newlength
        for i in range(self.size):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = self.size - 1
        self.size = newlength
        self.length = length
    def deallocate(self):
        newlength = self.size // 2
        length = self.length
        newQueue = [None] * newlength
        length = self.length
        for i in range(length):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = length - 1
        self.size = newlength
        self.length = length
    def __iter__(self):
        rlast = self.first + self.length
        for i in range(self.first,rlast):
            yield self.items[i % self.size]
    
    # define your function below
    def pop_vip(self):
        if self.isEmpty():
            return None
        min = self.popfront()
        for i in range(self.length):
            current = self.popfront()
            if min[1] > current[1]:
                self.pushback(min)
                min = current
            else:
                self.pushback(current)
        return min

a=Fifo()
a.pushback(5)
a.pushback(6)
a.pushback(3)
print(a.popfront())
print(a.popfront())
print(a.popfront())