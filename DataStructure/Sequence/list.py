#继承
import time
import numpy as np
class PyList(list):
    def __init__(self,contents=[],size=20):  #__init__ 重载init
        self.items=[None]*size #初始化空间
        self.numItems=0        #实际放的
        self.size = size       #列表实际的大小
        for e in contents:
            self.append(e)     #这一步并没有加入a里面来

    def __contains__(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True 
        return False
    

    def __eq__(self,other):             #重载了in,可用添加print验证
        if type(other) != type(self):
            return False
        if self.numItems != other.numItems:
            return False
        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __setitem__(self,index,val):
        if index>=0 and index<self.numItems:
            self.items[index] = val
            return
        raise IndexError("PyList assignment index out of range")
    
    def __getitem__(self,index):
        if index>=0 and index<self.numItems:
            return self.items[index]
        raise IndexError("PyList index out of range")

    def __add__(self,other):
        result = PyList(size = self.numItems+other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
        for i in range(other.numItems):
            result.append(other.items[i])
        return result

    def __worst__(self):  #Consider the above case
        result = PyList([], size = self.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
            result.delete(self.numItems-1)
        return result

    def append(self,item):             
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1

    def pushfront(self,item):
        if self.numItems == self.size:
            self.allocate()
        for i in range(self.numItems-1,-1,-1):
            self.items[i+1]=self.items[i]
        self.items[0] = item
        self.numItems += 1


    def allocate(self):
        newlength = 2*self.size  #空间默认扩大一倍
        newList = [None]*newlength
        for i in range(self.numItems):
            newList[i] = self.items[i]
        self.items = newList
        self.size = newlength

    def insert(self,i,x):
        if self.numItems == self.size:
            self.allocate()
        if i<self.numItems:
            for j in range(self.numItems-1,i-1,-1):   #反向遍历
                self.items[j+1]=self.items[j]
            self.items[i] = x
            self.numItems +=1
        else:
            self.append(x)#加到队尾
    
    def delete(self,index):
        if self.numItems == self.size/4:
            self.deallocate()
        if index <= self.numItems:
            for j in range(index,self.numItems-1):
                self.items[j] = self.items[j+1]
            self.numItems -=1
        else:
            raise IndexError("PyList index out of range")

    def deallocate(self):
        newlength = self.size/2
        newList = [None]*newlength
        for i in range(self.numItems):
            newList[i] = self.items[i]
        self.items = newList
        self.size = newlength



    def delete_last(self,k):
        if k > self.numItems:
            raise IndexError("PyList index out of range")
        if(k>0):
            self.numItems = self.numItems-k
            if self.numItems <=self.size//4: #resize operation
                newlength = 2*self.numItems
                newList = [None]*newlength
                for i in range(self.numItems):
                    newList[i] = self.items[i]
                self.items = newList
                self.size = newlength      
        else:
            raise IndexError("Do not exist such k")



    def popback(self):
        if self.numItems == self.size/4:
            self.deallocate()
        result = self.items[self.numItems-1]
        self.numItems -=1
        return result

    def popfront(self):
        if self.numItems == self.size/4:
            self.deallocate()
        result = self.items[0]
        for j in range(0,self.numItems-2):
            self.items[j] = self.items[j+1]
        self.numItems -=1
        return result

    def findmax(self,n):
        if n == 1:
            return self.items[0]
        else:
            m = self.findmax(n-1)
            return m if m>self.items[n-1] else self.items[n-1]
    
    def selectsort(self):
        outlist=PyList([],size=self.size)
        k=self.numItems
        while k>0:
            index=0
            min = self.items[0]
            for i in range(self.numItems):
                if min > self.items[i]:
                    min = self.items[i]
                    index = i
            outlist.append(min)
            self.delete(index)
            k-=1
        return outlist


    def qsort(self):
        if self.numItems <= 1:
            return self
        pivot = self.items[0]
        list1 = PyList([],self.numItems)
        listp = PyList([],self.numItems)
        list2 = PyList([],self.numItems)
        for i in range(self.numItems):
            if self.items[i] < pivot:
                list1.append(self.items[i])
            else:
                if self.items[i] == pivot:
                    listp.append(self.items[i])
                else:
                    list2.append(self.items[i])
        
        slist1 = list1.qsort()
        slist2 = list2.qsort()
        return slist1+listp+slist2

    def partition(self,low,high):
        i = low -1
        pivot = self.items[high]
        for j in range(low,high):
            if self.items[j] <= pivot:
                i=i+1
                self.items[i],self.items[j] = self.items[j],self.items[i]
        self.items[i+1],self.items[high] = self.items[high],self.items[i+1]
        return (i+1)
    
    def quickSort(self,low,high):
        if low < high:
            pi = self.partition(low,high)

            self.quickSort(low,pi-1)
            self.quickSort(pi+1,high)


    def radixsort(self):
        list0=PyList([0]*1000,size=10000)
        list1=PyList([],size=20000)
        #生成桶
        for i in range(self.numItems):
            list0[self.items[i]] +=1

        for j in range(list0.numItems):
            if list0.items[j] !=0:
                for num in range(list0.items[j]):
                    list1.append(j)
                num-=1  #单纯为了防止warning
        return list1

    def Merge(self,left,pivot,right):
        temp = PyList([0]*1000,size=2000)
        i=left
        j=pivot+1
        k=0
        while (k<=right-left):
            if(i==pivot+1):
                j+=1
                temp.items[k] = self.items[j]
                i +=1
                j +=1
                continue

            if(j==right+1):
                i+=1
                temp.items[k] = self.items[i]
                i +=1
                j +=1
                continue

            if(self.items[i] < self.items[j]):
                i+=1
                temp.items[k]=self.items[i]
            else:
                j+=1
                temp.items[k] = self.items[j]
            k+=1
        i=left
        j=0
        while (i<=right):
            self.items[i] = temp.items[j]
            i +=1
            j +=1
    
    def MergeSort(self,start,end):
        if (start<end):
            i=(end+start)//2
            self.MergeSort(start, i)
            self.MergeSort(i+1, end)
            self.Merge(start,i,end)

    def radixSort(self, numdigits, digits):
        sortedlist = self
        for i in range(numdigits):
            sortedlist = sortedlist.Ksort(i,digits)
        return sortedlist
        
    def Ksort(self,round,digits):
        bucket = PyList(size=digits)
        for k in range(digits):
            newlist = PyList(size = self.numItems)
            bucket.append(newlist)
        for i in range(self.numItems):
            item = self.items[i]
            item1 = item // (digits **round)%digits
            bucket[item1].append(item)
        result = bucket[0]
        for k in range(digits-1):
            result = result + bucket[k+1]
        return result
    
    def __merge(former,latter):
        i = 0
        j = 0
        res=PyList([],former.numItems + latter.numItems)
        while former.numItems > i and latter.numItems > j :
            if former[i] <= latter[j]:
                res.append(former[i])
                i = i + 1
            else:
                res.append(latter[j])
                j = j + 1
        if i == former.numItems:
            for m in range(j,latter.numItems):
                res.append(latter[m])
            
        if j == latter.numItems:
            for m in range(i,former.numItems):
                res.append(former[m])
        return res

    def mergesort(self,threshold = 1):
        if self.numItems <= threshold:
            #self.sort()
            return self
        list1 = PyList([],self.numItems)
        list2 = PyList([],self.numItems) 
        cursor = self.numItems//2
        for i in range(0,cursor):
            list1.append(self.items[i])
        for i in range(cursor,self.numItems):
            list2.append(self.items[i])
        list1 = list1.mergesort(threshold)
        list2 = list2.mergesort(threshold)
        return PyList.__merge(list1,list2)
    
def merge_sort(arr):
    beg=time.time()
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    result = merge(merge_sort(left),merge_sort(right))
    end=time.time()
    print("运行时间:",end-beg)
    return result

def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


#d=SPYLIST(['a','b','c'],[1,2,3])
newlist = PyList([4,1,5,3,2],size=100)
print(newlist)
print("验证schewe快速排序：")
newsort = newlist.qsort()
for i in range(newsort.numItems):
    print(newsort.__getitem__(i))
newlist1 = PyList([4,1,5,3,2],size=100)
print("验证删除k")
newlist1.delete_last(3)
print(newlist1.numItems)

print("fenjiexian")
a=PyList([1,2,3,4],size=4)
b=PyList([1,2,3,4,5],size=5)
c=PyList([1,2,3,4,5],size=10)
e=PyList([1,2,3,4,5,6],size=10)
d=[1,2,3,4]
g=PyList([4,1,5,3,2],size=100)
h=PyList([4,1,5,3,2],size=100)
h.delete_last(3)
for i in range(h.numItems):
    print(h.__getitem__(i))
res=g.selectsort()
print("输出排序结果")
for i in range(res.numItems):
    print(res.__getitem__(i))

print("测试mergesort")
g.MergeSort(0,g.numItems-1)
for i in range(g.numItems):
    print(g.__getitem__(i))
test0=[8,6,4,2,6,8,9,1,0]
res0=merge_sort(test0)
print(res0)


print("测试桶排序")
test = PyList([4,5,1,3,2,6,5,3],size=2000)
test1=test.radixsort()
for i in range(test1.numItems):
    print(test1.__getitem__(i))
print("c的长度")
print(d[1:2])
print ("是否相等", a.__eq__(b))
print("是否包含",a.__contains__(1))

a.append(3)

a.append(5)
print("a的大小",a.size)
print("insert操作和输出")
a.insert(0,5)
for i in range(a.numItems):
    print(a.__getitem__(i))

print("delete操作和输出")
a.delete(3)
for i in range(a.numItems):
   print(a.__getitem__(i))

#print('b的输出')
#b.delete_last(9)

print('c的输出')
c.pushfront(0)
for i in range(c.numItems):
    print(c.__getitem__(i))

print("快速排序e")
e.quickSort(0,e.numItems-1)
for i in range(e.numItems):
    print(e.__getitem__(i))