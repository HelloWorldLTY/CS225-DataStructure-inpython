class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class SplayTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def RightRotate(self, x):  # x为根节点
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def LeftRotate(self, x):  # x为根节点
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
       """
       如果键存在于树中，则将键置于树根位置
       如果键不存在，那么将把最后一个被访问的项放在树根
       """
       if root is None or root.key == key:
           # 没有根或者树根为key则对根进行splay
            return root
       if root.key > key:  # key在左子树中
            if root.left is None:  # 左子树为空，则返回唯一访问的根节点
                return root
            if root.left.key > key:  # Zig-Zig (Left Left)
                # 首先递归地把key移至左子树的左子树的根
                root.left.left = self.splay(root.left.left, key)
                # 第一次对根右旋，第二次是在执行else之后才可能进行右旋
                root = self.RightRotate(root)
            elif root.left.key < key:  # Zig-Zag (Left Right)
                root.left.right = self.splay(root.left.right, key)
                root.left = self.LeftRotate(root.left)
            # LR情况：对调整之后的根在进行右旋
            return root if root.left is None else self.RightRotate(root)
       else:  # key在右子树中
            if root.right is None:  # 右子树为空，则返回唯一访问的根节点
                return root
            if root.right.key > key:  # Zig-Zag (Right Left)
                # 首先递归地把key移至右子树的左子树的根
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.RightRotate(root.right)
            elif root.right.key < key:  # Zag-Zag (Right Right)
                    root.right.right = self.splay(root.right.right, key)
                    root = self.LeftRotate(root)
            # RL情况：对调整之后的根在进行左旋
            return root if root.right is None else self.LeftRotate(root)

    def search(self, key):
    	self.root = self.splay(self.root, key)

    def insert(self, key):
        self.size += 1
        return self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:  # 数空情况
            return Node(key)
        # 像访问要访问的节点置于根节点
        root = self.splay(root, key)
        if root.key == key:  # 如果根节点==key，那么直接返回根节点
            return root
        new = Node(key)
        if root.key > key:
            # 如果根节点的key＞key，那么就把根节点作为其右子树，根节点的左子树作为new的左子树
            new.right = root
            new.left = root.left
            root.left = None
        else:
            new.left = root
            new.right = root.right
            root.right = None
        return new  # 返回新的根节点

    def preorder(self, subtree):
        if subtree is not None:
            print(subtree.key, end=' ')
            self.preorder(subtree.left)
            self.preorder(subtree.right)

if __name__=='__main__':
    sp = SplayTree()
    for i in range(1,10):
        sp.root=sp.insert(i)
    sp.preorder(sp.root) 
    sp.search(5)
    print(sp.root.key) 
    sp.preorder(sp.root) 