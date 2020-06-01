'''
class HashSet:
    def __init__(self, contents = []):
        self.items = [None]*20
        self.numItems = 0
        for e in contents:
            self.add(e)
    
    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False
    def __add(item,items):
        index = hash(item)%len(items)
        location = -1
        while items[index] != None:
            if items[index] != None:
                return False
            if location <0 and type(items[index]) == HashSet.__Placeholder():
                location = index
            index = (index+1)%len(items)
        if location <0:
            loaction = index
        items[location] = item
        return True

    def __rehash(olditems, newitems):
        for e in olditems:
            if e != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newitems)
        return newitems

    def __contains__(self, item):
        index = hash(item) % len(self.items)
        while self.items[index] != None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)
        return False
    
    def delete(self,item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1 
            load = max(self.numItems,20) / len(self.items) 
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*(len(self.items) // 2)) 
        else:
            raise KeyError("Item not in HashSet")
        
    def __remove(item,items):
        index = hash(item) % len(items)
        while items[index] != None:
            if items[index] == item:
                nextIndex = (index+1)%len(items)
                if items[nextIndex] == None:
                    items[index] = None
                else:
                    items[index] = HashSet.__Placeholder()
                return True
            index = (index + 1) % len(items)
        return False
'''

a=[[1,1,1],[2,2,2],[3,3,3],[4,4]]
a.append([4])
for i in a:
    print(i[0])
print(a)