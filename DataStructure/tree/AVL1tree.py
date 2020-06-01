class AVLTree:
    class AVLNode:
        def __init__(self,item,balance=0,left=None,right=None):
            self.item = item
            self.balance = balance
            self.left = left
            self.right = right
            self.parent = None
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
            yield self.item, self.balance
            if self.right != None:
                for elem in self.right:
                    yield elem
        def __repr__(self):#解释器，返回对象的string格式
            return "AVLTree.AVLNode("+repr(self.item)+",balance="+repr(self.balance)+",left="+repr(self.left)+",right="+repr(self.right)+")"

    def __init__(self):
        self.root = None
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __rotateLeft(node,child,nbal,cbal):
            node.setRight(child.getLeft())
            node.setbal(nbal)
            child.setLeft(node)
            child.setbal(cbal)
            return child
    def __rotateRight(node,child,nbal,cbal):
            node.setLeft(child.getRight())
            node.setbal(nbal)
            child.setRight(node)
            child.setbal(cbal)
            return child

    def insert(self,item):
        def __insert(root,item):
            newtree = AVLTree.AVLNode(item)
            stack = []
            badChild = None
            while root != None:
                if item < root.getitem():
                    print(root)
                    stack.insert(0,(root,-1))
                    if root.getLeft() == None:
                        root.setLeft(newtree)
                        return (stack,badChild)
                    if root.getbal() == -1:
                        badChild = root.getLeft()
                    root = root.getLeft()
                else:       
                    stack.insert(0,(root,1))
                    if root.getRight() == None:
                        root.setRight(newtree)
                        return (stack,badChild)
                    if root.getbal() == 1:
                        badChild = root.getRight()
                    root = root.getRight()
                    
        if self. root == None:
            self.root = AVLTree.AVLNode(item)
            stack = []
            badChild = None
        else:
            result = __insert(self.root,item)
            stack = result[0]
            badChild = result[1]
        rotTree = None
        for N in stack:
            #print(N)
            node = N[0]
            #print('node',node)
            inc = N[1]
            if rotTree != None:
                if inc == 1:
                    node.setRight(rotTree)
                else:
                    node.setLeft(rotTree)
                return

            newbal = node.getbal() + inc
            
            if badChild == node:
                if inc == 1:
                    badGrandchild = node.getRight()
                else:
                    badGrandchild = node.getLeft()
            if newbal == 0:
                node.setbal(0)
                return
            if -1 <= newbal <= 1:
                node.setbal(newbal)
            else:
                if inc == 1:
                    if badChild.getRight() == badGrandchild:
                        rotTree = AVLTree.__rotateLeft(node,badChild,0,0)
                    else:
                        if item < badGrandchild.getitem():
                            n,c = 0,1
                        else:
                            if item > badGrandchild.getitem():
                                n,c = -1,0
                            else:
                                n,c = 0,0
                        rotTree1 = AVLTree.__rotateRight(badChild,badGrandchild,c,0)
                        rotTree = AVLTree.__rotateLeft(node,rotTree1,n,0)
                else:
                    if badChild.getLeft() == badGrandchild:
                        rotTree = AVLTree.__rotateRight(node,badChild,0,0)
                    else:
                        if item < badGrandchild.getitem():
                            n,c = 0,-1
                        else:
                            if item > badGrandchild.getitem():
                                n,c = 1,0
                            else:
                                n,c = 0,0
                        rotTree1 = AVLTree.__rotateLeft(badChild,badGrandchild,c,0)
                        rotTree = AVLTree.__rotateRight(node,rotTree1,n,0)

        if rotTree != None:
            self.root = rotTree
            
    def find(self,item):
        def __find(root,item):
            if root == None:
                return False
            if item == root.getitem():
                return True
            if item < root.getitem():
                return __find(root.getLeft(),item)
            else:
                return __find(root.getRight(),item)
        return __find(self.root,item)

    def print_AVL(self):
        ret = self.print_tree(self.root, 0, 0,{})
        ret = sorted(ret.items(), key=lambda x: x[1])
        cur_x = 0
        cur_y = 0
        for item in ret:
            x = item[1][1]
            y = item[1][0]
            parent = item[1][2]
            for i in range(cur_y, y):
                print('\n')
                cur_x = 0
            for i in range(cur_x, x):
                print(' ', end='')
            print(item[0], end='')
            print('('+str(parent)+')',end = '')
            cur_x = x+1
            cur_y = y
        print('\n')
    # helper function
    def print_tree(self, root, x, y, ret):
        # none do nothing and return
        if(root == None):
            return ret
        if(root.left == None and root.right == None): # leaf node   
            ret[str(root.item)] = (y, x, root.parent.item)
            return ret
        # otherwise, the left or right node is not None
        if(x-8 < 0):
            x = 8
        if(root.left != None):
            root.left.parent = root
            ret = self.print_tree(root.left, x-8, y+1, ret)
            leftChild = str(root.left.item)
            if(root == self.root):
                x = ret[leftChild][1]+16 # to distinct left and right tree
            else:
                x = ret[leftChild][1]+8
        if(root.parent == None):
            ret[str(root.item)] = (y, x, None)
        else:
            ret[str(root.item)] = (y, x, root.parent.item)
        if(root.right != None):
            root.right.parent = root
            if(root == self.root):
                ret = self.print_tree(root.right, x+16, y+1, ret) # to distinct left and right tree
            else:
                ret = self.print_tree(root.right, x+8, y+1, ret)
        return ret

    # original AVL tree class change to Fibo

class FibTree:
    class FibNode:
        def __init__(self,item,balance=0,left=None,right=None):
            self.item = item
            self.balance = balance
            self.left = left
            self.right = right
            self.parent = None
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
            yield self.item, self.balance
            if self.left != None:
                for elem in self.left:
                    yield elem
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "FibTree.FibNode("+repr(self.item)+",balance="+repr(self.balance)+",left="+repr(self.left)+",right="+repr(self.right)+")"

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __rotateLeft(node,child,nbal,cbal):
            node.setRight(child.getLeft())
            node.setbal(nbal)
            child.setLeft(node)
            child.setbal(cbal)
            return child
    def __rotateRight(node,child,nbal,cbal):
            node.setLeft(child.getRight())
            node.setbal(nbal)
            child.setRight(node)
            child.setbal(cbal)
            return child

    def insert(self,item):
        def __insert(root,item):
            newtree = FibTree.FibNode(item)
            stack = []
            badChild = None
            while root != None:
                if item < root.getitem():
                    stack.insert(0,(root,-1))
                    if root.getLeft() == None:
                        root.setLeft(newtree)
                        return (stack,badChild) # return the problem one
                    if root.getbal() == -1:
                        badChild = root.getLeft()
                    root = root.getLeft()
                else:       
                    stack.insert(0,(root,1))
                    if root.getRight() == None:
                        root.setRight(newtree)
                        return (stack,badChild) # return the problem one
                    if root.getbal() == 1:
                        badChild = root.getRight()
                    root = root.getRight()
    
        if self. root == None:
            self.root = FibTree.FibNode(item)
            stack = []
            badChild = None
        else:
            result = __insert(self.root,item)
            stack = result[0]
            badChild = result[1]
        rotTree = None
        for N in stack:
            print(stack)
            node = N[0]
            inc = N[1]
            if rotTree != None:
                if inc == 1:
                    node.setRight(rotTree)
                else:
                    node.setLeft(rotTree)
                return
            
            newbal = node.getbal() + inc
            if badChild == node:
                if inc == 1:
                    badGrandchild = node.getRight()
                else:
                    badGrandchild = node.getLeft()
            if newbal == 0:
                node.setbal(0)
                return
            if -1 <= newbal <= 1:
                node.setbal(newbal)
            else:
                if inc == 1:
                    if badChild.getRight() == badGrandchild:
                        rotTree = FibTree.__rotateLeft(node,badChild,0,0)
                    else:
                        if item < badGrandchild.getitem():
                            n,c = 0,1
                        else:
                            if item > badGrandchild.getitem():
                                n,c = -1,0
                            else:
                                n,c = 0,0
                        rotTree1 = FibTree.__rotateRight(badChild,badGrandchild,c,0)
                        rotTree = FibTree.__rotateLeft(node,rotTree1,n,0)
                else:
                    if badChild.getLeft() == badGrandchild:
                        rotTree = FibTree.__rotateRight(node,badChild,0,0)
                    else:
                        if item < badGrandchild.getitem():
                            n,c = 0,-1
                        else:
                            if item > badGrandchild.getitem():
                                n,c = 1,0
                            else:
                                n,c = 0,0
                        rotTree1 = FibTree.__rotateLeft(badChild,badGrandchild,c,0)
                        rotTree = FibTree.__rotateRight(node,rotTree1,n,0)
        if rotTree != None:
            self.root = rotTree
    def find(self,item):
        def __find(root,item):
            if root == None:
                return False
            if item == root.getitem():
                return True
            if item < root.getitem():
                return __find(root.getLeft(),item)
            else:
                return __find(root.getRight(),item)
        return __find(self.root,item)
    
    def delete(self,item):
        def __findandreturn(root,item):
            if root == None:
                return([],root,False)
            if item == root.getitem():
                return([(root,0)],root,True)
            if item < root.getitem():
                result = __findandreturn(root.getLeft(),item)
                stack1 = result[0]
                stack1.append((root,1))
                return (stack1,result[1],result[2])
            else:
                result = __findandreturn(root.getRight(),item)
                stack1 = result[0]
                stack1.append((root,-1))
                return (stack1,result[1],result[2])

        def __findswapLeft(node,prev):
            stack = []
            while node.getLeft() != None:
                stack.insert(0,(node,1))
                prev = node
                node = node.getLeft()
            minitem = node.getitem()
            if stack == []:
                prev.setRight(node.getRight())
            else:
                prev.setLeft(node.getRight())
            return (minitem,stack)


        def __findswapRight(node,prev):
            stack = []
            while node.getRight() != None:
                stack.insert(0,(node,-1))
                prev = node
                node = node.getRight()
            maxitem = node.getitem()
            if stack == []:
                prev.setLeft(node.getRight())
            else:
                prev.setRight(node.getLeft())
            return (maxitem,stack)

        result = __findandreturn(self.root,item)
        if result[2] == False:
            return
        stack1 = result[0]
        start = stack1.pop(0)
        startnode = start[0]
        startinc = start[1]
        nextRight = startnode.getRight()
        nextLeft = startnode.getLeft()
        stack = []
        if startnode.getbal() == 1:
            result = __findswapLeft(nextRight,startnode)
            stack = result[1]
            startnode.setitem(result[0])
            startinc = -1
        else:
            if startnode.getbal() == -1:
                result = __findswapRight(nextLeft,startnode)
                stack = result[1]
                startnode.setitem(result[0])
                startinc = 1
            else:
                if startnode.getRight() != None:
                    if nextRight.getbal() != 1:
                        result = __findswapLeft(nextRight,startnode)
                        stack = result[1]
                        startnode.setitem(result[0])
                        startinc = -1
                    else:
                        result = __findswapRight(nextLeft,startnode)
                        stack = result[1]
                        startnode.setitem(result[0])
                        startinc = 1
                else:
                    if self.root == startnode:
                        self.root = None
                        return
                    last = stack1.pop(0)
                    lastnode = last[0]
                    if last[1] ==1:
                        lastnode.setLeft(None)
                    else:
                        lastnode.setRight(None)
                    stack1.insert(0,(lastnode,last[1]))
                    startnode = None
        if startnode != None:
            start = (startnode,startinc)
            stack1.insert(0,start)
        stack = stack + stack1
        stack2 = iter(stack+[(None,0)])
        NN = next(stack2)
        for N in stack:
            currentnode = N[0]
            increment = N[1]
            NN = next(stack2)
            rotTree = None
            stop = False
            newbal = currentnode.getbal() + increment
            if -1 <= newbal <= 1:
                currentnode.setbal(newbal)
                if newbal != 0:
                    return
            else:
                if increment == 1:
                    badChild = currentnode.getRight()
                    badGrandchild = badChild.getLeft()
                    if badChild.getbal() == 0:
                        rotTree = FibTree.__rotateLeft(currentnode,badChild,1,-1)
                        stop = True
                    else:
                        if badChild.getbal() == 1:
                            rotTree = FibTree.__rotateLeft(currentnode,badChild,0,0)
                        else:
                            nbal,cbal = 0,0
                            if badGrandchild.getbal() == 1:
                                nbal = -1
                            if badGrandchild.getbal() == -1:
                                cbal = 1
                            rotTree1 = FibTree.__rotateRight(badChild,badGrandchild,cbal,0)
                            rotTree = FibTree.__rotateLeft(currentnode,rotTree1,nbal,0)
                else:
                    badChild = currentnode.getLeft()
                    badGrandchild = badChild.getRight()
                    stop = False
                    if badChild.getbal() == 0:
                        rotTree = FibTree.__rotateRight(currentnode,badChild,-1,1)
                        stop = True
                    else:
                        if badChild.getbal() == -1:
                            rotTree = FibTree.__rotateRight(currentnode,badChild,0,0)
                        else:
                            nbal,cbal = 0,0
                            if badGrandchild.getbal() == 1:
                                cbal = -1
                            if badGrandchild.getbal() == -1:
                                nbal = 1
                            rotTree1 = FibTree.__rotateLeft(badChild,badGrandchild,cbal,0)
                            rotTree = FibTree.__rotateRight(currentnode,rotTree1,nbal,0)
            if rotTree != None:
                if NN[0] != None:
                    if NN[1] == 1:
                        NN[0].setLeft(rotTree)
                    if NN[1] == -1:
                        NN[0].setRight(rotTree)
                else:
                    self.root = rotTree
            if stop == True:
                return
        
    
    
    ## Add a function to print out the tree intuitionistically
    def print_AVL(self):
        ret = self.print_tree(self.root, 0, 0,{})
        ret = sorted(ret.items(), key=lambda x: x[1])
        cur_x = 0
        cur_y = 0
        for item in ret:
            x = item[1][1]
            y = item[1][0]
            parent = item[1][2]
            for i in range(cur_y, y):
                print('\n')
                cur_x = 0
            for i in range(cur_x, x):
                print(' ', end='')
            print(item[0], end='')
            print('('+str(parent)+')',end = '')
            cur_x = x+1
            cur_y = y
        print('\n')
    # helper function
    def print_tree(self, root, x, y, ret):
        # none do nothing and return
        if(root == None):
            return ret
        if(root.left == None and root.right == None): # leaf node   
            ret[str(root.item)] = (y, x, root.parent.item)
            return ret
        # otherwise, the left or right node is not None
        if(x-8 < 0):
            x = 8
        if(root.left != None):
            root.left.parent = root
            ret = self.print_tree(root.left, x-8, y+1, ret)
            leftChild = str(root.left.item)
            if(root == self.root):
                x = ret[leftChild][1]+16 # to distinct left and right tree
            else:
                x = ret[leftChild][1]+8
        if(root.parent == None):
            ret[str(root.item)] = (y, x, None)
        else:
            ret[str(root.item)] = (y, x, root.parent.item)
        if(root.right != None):
            root.right.parent = root
            if(root == self.root):
                ret = self.print_tree(root.right, x+16, y+1, ret) # to distinct left and right tree
            else:
                ret = self.print_tree(root.right, x+8, y+1, ret)
        return ret

tree=AVLTree()
a=[1,3,4,5,7,8,9]
for i in range(1,11):
    tree.insert(i)
tree.print_AVL()

for i in tree:
    print(i) #括号里是父亲的值
