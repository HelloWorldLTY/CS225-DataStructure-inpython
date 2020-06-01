class DLinkedList:
    class __Node:
        def __init__(self, item, next=None, previous = None):
            self.item = item
            self.next = next
            self.previous = previous
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def getPrevious(self):
            return self.previous
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next
        def setPrevious(self,previous):
            self.previous = previous

    def __init__(self, contents = []):
        self.first = DLinkedList.__Node(None, None, None)   #dummy node
        self.numItems = 0
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        for e in contents:
            self.append(e)
    
    def append(self, item):
        lastNode = self.first.getPrevious()
        newNode = DLinkedList.__Node(item,self.first,lastNode)
        lastNode.setNext(newNode)
        self.first.setPrevious(newNode)
        self.numItems += 1

    def locate(self, index):
        if index >= 0 and index <self.numItems:
            cursor = self.first.getNext()
            for k in range(index):
                cursor = cursor.getNext()
            return cursor
        raise IndexError('DLinkedList index out of range')

    def splice(self, index, other, index1, index2):
        if index1 <= index2:
            begin = other.locate(index1)
            end = other.locate(index2)
            self.insertList(begin,end,index)

    def insertList(self,begin,end,index):
        address   = self.locate(index)
        successor = address.getNext()
        begin.setPrevious(address)
        end.setNext(successor)
        address.setNext(begin)
        successor.setPrevious(end)

    def SelectionSort(self):
        firstNode = self.first.getNext()
        lastNode = self.first.getPrevious()
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        counter = self.numItems
        last = self.first
        while counter !=0 :
            location = self.getMinimum(firstNode, lastNode)
            if location == firstNode:
                firstNode = location.getNext()
            else:
                if location == last:
                    lastNode = location.getPrevious()
                else:
                    self.cut(firstNode,lastNode,location)
            self.addLocation(last, location)
            last = location
            counter -=1

    def getMinimum(self, first, last):
        minimum = first.getItem()
        cursor = first
        location = first
        while cursor != last:
            cursor = cursor.getNext()
            item = cursor.getItem()
            if item < minimum:
                minimum = item
                location = cursor
        return location

    def cut(self, first, last, location):
        if location == first:
            first = location
        else:
            if location ==last:
                last = location
            else:
                prev = location.getPrevious()
                next = location.getNext()
                prev.setNext(next)
                next.setPrevious(prev)

    def addLocation(self, outlast, location):
        location.setPrevious(outlast)
        location.setNext(self.first)
        outlast.setNext(location)
        self.first.setPrevious(location)

    def InsertionSort(self):
        cursor = self.first.getNext() 
        self.first.setNext(self.first) 
        self.first.setPrevious(self.first) 
        while cursor != self.first:
            cursor1 = cursor.getNext()
            self.addout(cursor)
            cursor = cursor1

    def addout(self,cursor):
        cursor2 = self.first.getNext()
        while cursor2.getItem() < cursor.getItem() and cursor2.getNext() != self.first:
            cursor2 = cursor2.getNext()
        if cursor2.getItem() >= cursor.getItem():
            previous = cursor2.getPrevious()
            previous.setNext(cursor)
            cursor.setNext(cursor2)
            cursor.setPrevious(previous)
            cursor2.setPrevious(cursor)
        else:
            cursor2.setNext(cursor)
            cursor.setNext(self.first)
            cursor.setPrevious(cursor2)
            self.first.setPrevious(cursor)


    #exchange the data scope of Dlinkedlist
    def bubblesort(self):
        if self.numItems ==0 or self.numItems == 1:
            return self
        p1=self.first.getNext()
        while( p1 != self.locate(self.numItems-1)):
            p2 = p1.getNext()
            while(p2 != self.locate(self.numItems-1)):
                if (p1.getItem() < p2.getItem()):
                    res1=p1.getItem()
                    res2=p2.getItem()
                    p1.setItem(res2)
                    p2.setItem(res1)
                p2=p2.getNext()
            p1=p1.getNext()

 #self.append = self.splice(self.numItems-1, other([7]), 0, 0)               
resu=DLinkedList([1,2,3,4,5])
resu.bubblesort()






            

        
