class BST:
    class __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self,newval):
            self.item = newval
        def getLeft(self):
            return self.left
        def setLeft(self,newleft):
            self.left = newleft
        def getRight(self):
            return self.right
        def setRight(self,newright):
            self.right = newright
        
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem

        def getsubtree(self,val):
            result=[]
            if self.left != None:
                for elem in self.left:
                    result.append(elem)
            result.append(self.val)
            if self.right != None:
                for elem in self.right:
                    result.append(elem)
            result.remove(val)
            return result
                
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        def __insert(root,val):
            if root == None:
                return BST.__Node(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
            else:
                root.setRight(__insert(root.getRight(),val))
            return root
        self.root = __insert(self.root, val)
    
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def find(self,val):
        def __find(root,val):
            if root == None:
                return False
            if val == root.getVal():
                return True
            if val < root.getVal():
                return __find(root.getLeft(), val)
            else:
                return __find(root.getRight(), val)
            return __find(self.root,val)

    def delete(self,val):
        def __delete(root,val):
            if root == None:
                return root
            if val == root.getVal():
                return __merge(root.getLeft(),root.getRight())
            if val <root.getVal():
                root.setLeft(__delete(root.getLeft(), val))
                return root
            root.setRight(__delete(root.getRight(), val))
            return root
            
        def __merge(leftnode,rightnode):
            if rightnode == None:
                return leftnode 
            if rightnode.getLeft() == None:
                rightnode.setLeft(leftnode)
                return rightnode 
            __merge(leftnode,rightnode.getLeft()) 
            return rightnode
        self.root = __delete(self.root,val)


tree=BST()
for x in [5,8,2,1,4,9,6,7]:
    tree.insert(x)
tree.delete(5)


for x in tree:
    print(x)
