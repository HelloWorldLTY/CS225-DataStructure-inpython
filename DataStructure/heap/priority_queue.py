#Help to test data    
import random
#Create a MaxHeap
class P_q():
    def __init__(self):
        self._data = []
        self._count = len(self._data)
 
    def size(self):
        return self._count
 
    def isEmpty(self):
        return self._count == 0
 
    def enqueue(self, item):
        # insert elements into the heap
        if self._count >= len(self._data):
            self._data.append(item)
        else:
            self._data[self._count] = item
 
        self._count += 1
        self._siftup(self._count-1)
 
    def dequeue(self):
        # pop out of the heap
        if self._count > 0:
            ret = self._data[0]
            self._data[0] = self._data[self._count-1]
            self._count -= 1
            self._siftDown(0)
            return ret
        
    def _siftup(self, index):
        # shift self._data[index] up, so that it will be not larger than parent node
        parent = (index-1)//2
        while index > 0 and self._data[parent][1] < self._data[index][1]:
            # swap
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent
            parent = (index-1)//2
 
    def _siftDown(self, index):
        #Shift self._data[index] down, so that it will be not smaller than child node
        j = 2*index + 1
        while j < self._count :
            # There exists child node
            if j+1 < self._count and self._data[j+1][1] > self._data[j][1]:
                # exist right child node
                j += 1
            if self._data[index][1] >= self._data[j][1]:
                # do not need to exchange
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = 2*index + 1
    
pq=P_q()
pq.enqueue((1,0))
pq.enqueue((2,-1))
pq.enqueue((3,1))
pq.enqueue((4,2))
pq.enqueue((4,3))
print(pq.dequeue())
