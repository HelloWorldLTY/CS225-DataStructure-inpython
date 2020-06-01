from AVL_Tree import AVLTree
import random
import os

path = './tree_pic'
if not os.path.exists(path):
    os.mkdir(path)

# 创建一个生成器, 做图片的名称
'''
g = (path + '/tree' + str(i) + '.png' for i in range(1, 30))
'''
t = AVLTree()
# lst = [random.randrange(20, 300) for i in range(20)]
lst = random.sample(range(30, 300), 20)
t.insert(lst)
print(lst)
#t.draw(next(g))
print(t.get_tree_state())
for i in range(8):
    k = random.choice(lst)
    print("删除键%d" % k)
    t.delete_key(k)
    print(t.get_tree_state())       # 打印树的高度, 元素个数，树是否平衡
    
    #t.draw(next(g))


t.insert(-5, 200, 300)
t.insert(10, 0, 410, 15, 500)
#t.draw(next(g))
print(t.get_tree_state())