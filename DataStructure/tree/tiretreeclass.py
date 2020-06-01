import sys
class Trie:
    class TrieNode:
        def __init__(self,item,next=None,follows=None): 
            self.item = item
            self.next = next
            self.follows = follows 
            
    def __init__(self):
        self.start = None
        self.contain=[] 
    def insert(self,item):
        self.start = Trie.__insert(self.start,item)
    def __insert(node,item): 
        if item == []:
            newnode = Trie.TrieNode("#")
            return newnode
        if node == None:
            key = item.pop(0)
#             print(key)
            newnode = Trie.TrieNode(key)
            newnode.follows = Trie.__insert(newnode.follows,item) 
            return newnode
        else:
            key = item[0]
#             print(key)
            if node.item == key:
                key = item.pop(0)
                node.follows = Trie.__insert(node.follows,item)
            else:
                node.next = Trie.__insert(node.next,item)
            return node
    # a print function which can print out structure of tries 
    # to help better understand
    def print_trie(self, root, level_f):
        if(root == None):
            return
        if(root.item != '#'):
            print(root.item, '-', end='')
        else:
            print(root.item, end='')  
        self.print_trie(root.follows, level_f+1)
        if(root.next!=None):
            print('\n')
            str_sp = ' '*level_f*3 
            print(str_sp+'|')
            print(str_sp, end='')
        self.print_trie(root.next,level_f)
        return

    def findall(self, root, level_f):
        if(root == None):
            return
        if(root.item != '#'):
            self.contain.append(root.item)
        self.findall(root.follows, level_f+1)
        if(root.next!=None):
            self.contain.append(root.next.item)
        self.findall(root.next,level_f)
        return
    
    def __contains(node,item): 
        if item == []:
            return True
        if node == None:
            return False
        key = item[0]
        if node.item == key:
            key = item.pop(0)
            return Trie.__contains(node.follows,item)
        return Trie.__contains(node.next,item)

    def __contains__(self,item):
        return Trie.__contains(self.start,item+["#"])   

    def delete(self,item):
        if self.__contains__(item):
            pass

             



treetest=Trie()
result=[]
result0=[]
result1=[]
fd = open("/Users/mac/Desktop/test0.txt","r")
for line in fd.readlines():
    result.append(line.split())

for i in result:
    for j in i:
        result0.append(j)

for m in result0:
    result1.append(list(m))
print(result1)
print(result0)
print(result)
for j in result1:
    treetest.insert(j)
treetest.print_trie(treetest.start,0)
print('\n')


treetest.findall(treetest.start,0)
print(treetest.contain)

for i in []:
    print('test')