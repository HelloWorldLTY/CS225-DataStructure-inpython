
def sublist(l1,l2):
    i=0
    j=0
    while j != len(l2):
        if i<len(l1):
            if l1[i] == l2[j]:
                i+=1
                j+=1
            else:
                j+=1    
        if i==len(l1):
            return 1
    return 0


def in_list(list1,num):
    for i in range(0,len(list1)):
        if num==list1[i]:
            return 1
    return 0


def isequal(list1,list2):
    if len(list1) == len(list2):
        for i in range(0,len(list1)):
            if list1[i] != list2[i]:
                return 0
        return 1
    return 0
def delete(list1,num):
    if len(list1)==0:
        return
    for j in range(num-1,len(list1)-1):
        list1[j]=list1[j+1]
    list1.pop(-1)

def concat(list1, list2):
    for i in range(0, len(list2)):
        list1.append(list2[i])
    return list1

def insert(list,index,num):
    list.append(None)
    for i in range(len(list)-1,index,-1):
        print(i)
        list[i]=list[i-1]
    list[index]=num
    

a=[1,2,3]
c=[1,2,3,4]
b=[1,2,3,4]
print(in_list(a,1))
print(sublist(a,b))
print(isequal(b,c))
print(isequal(a,c))
#delete(c,1)
#print(c)
#print(concat(a,c))
insert(b,1,1)
print(b)
