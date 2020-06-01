class AVLTree:
    class AVLNode:
        def __init__(self, item, balance,left,right):
            self.item = item
            self.balance = balance
            self.left = left
            self.right = right
        
        def getitem(self):
            return self.item 
        def setitem(self,newitem):
            self.item = newitem 
        def getbal(self):
            return self.balance
        def setbal(self,newbalance):
            self.balance = newbalance 
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
            if self.right !=  None:
                for elem in self.right: 
                    yield elem 
    def __init__(self):
        self.root = None
    def __repr__(self):
        return "AVLTree.AVLNode("+repr(self.item)+", balance="+repr(self.balance)+", left="+repr(self.left)+", right="+repr(self.right)+")"