
# coding: utf-8

# In[9]:

#数字各位之和输出为一位数字
#思路：将输入的数字从字符串变为数字，然后相加即可，主要的问题就在于字符串和数字的类型转化
def ifsuccess():
    print('输入数字')
    a = input()
    while True:
        n = len(str(a))
        if n == 1:
            break
        if n > 1:
            m = 0
            for i in str(a):
                m = m + int(i)
            a = m
    print('最后得到的数字为 %s '%a)

ifsuccess()


# In[4]:

#判断是否能成为三角形，并且找出其中周长最大的组合
#这个问题其实很简单，先将输入的数字进行从大到小排序，判断相连的前三个数字，若是a<b+c ,则三角形成立，且一定是周长最大的（因为前面已经是从大到小排序）
#若是a>b+c,那么若是a为三角形的一个边，则后面没有可以和a组成三角形的边，因此应该将这三个相连的取值后移一位循环寻找可组成的三角形。
def findABC(a,b,c):
    if a<(b+c):
        return int(a)+int(b)+int(c)
    else:
        return False
        
def ifDelta():
    a = input()
    a = list(a)
    a.sort(reverse = True)
    print(a)
    for i in range(0,len(a)-2):
        m = i+1
        n = m+1
        if findABC(int(a[i]),int(a[m]),int(a[n])):
            break
    if findABC(int(a[i]),int(a[m]),int(a[n])):
        print('组合为:%s %s %s ' %(a[i],a[m],a[n]))
        print('周长为 : %d'%findABC(int(a[i]),int(a[m]),int(a[n])))
    else:
        print('不成立')
        
ifDelta()


# In[76]:

#判断A是否为B的树子串
#思路是将A、B分别先序遍历然后中序遍历 ，然后进行字符串匹配 。难点在于树的三种遍历还会不会写，需要使用递归

class Node:
    def __init__(self,value = None,left = None,right = None):
        self.right = right
        self.left = left
        self.value = value
#前序遍历
def preOrder(a,list_a):
    if a == None:
        return
    list_a.append(a.value)
    preOrder(a.left,list_a)
    preOrder(a.right,list_a)
#中序遍历
def midOrder(a,list_a):
    if a == None:
        return
    midOrder(a.left,list_a)
    list_a.append(a.value)
    midOrder(a.right,list_a)
#后序遍历
def afterOrder(a,list_a):
    if a == None:
        return
    afterOrder(a.left,list_a)
    afterOrder(a.right,list_a)
    list_a.append(a.value)
    #return list_after_A.append(a.value)

A = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
B = Node('B',Node('A'),Node('C'))
#判断是否为子串
def ifHave(a,b):
    length_a = len(a)
    length_b = len(b)
    ifhave = False
    count = 0
    for num_a in range(0,length_a-length_b):
        if not ifhave:
            if a[num_a] == b[0]:
                count = 1
                for m in range(1,length_b):
                    if a[num_a+1] == b[m]:
                        num_a = num_a+1
                        m = m+1
                        count = count + 1
                        if count == length_b:
                            ifhave = True
                            return True
                    else:
                        break
            else:
                print('匹配不成功')
#测试的二叉树
A = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
B = Node('B',Node('A'),Node('C'))

list_a_after = []
list_b_after = []
list_a_mid = []
list_b_mid = []
afterOrder(A,list_a_after)
afterOrder(B,list_b_after)
midOrder(A,list_a_mid)
midOrder(B,list_b_mid)

if ifHave(list_a_after,list_b_after)and ifHave(list_a_mid,list_b_mid):
    print('是子串')
else:
    print('不是子串')
    
#整个题目除了要进行遍历之外，还有就是输入的数组变成树结构,也就是说，上面的代码只能做到判断，还不能将输入转化成为二叉树结构

#a_Tree = input()
#b_Tree = input()


# In[6]:

#给出后序遍历，判断是否为二叉搜索树（即节点的右孩子都小于节点，节点的左孩子都大于节点）
#考的时候没想出来 现在有思路了 后序遍历是左右中的性质 因此最后的一个数是为根节点，那么右子树应该都大于根节点，左子树应该都大于根节点
#接下来继续对右子树和左子树进行循环判定就可以判断是否为二叉搜索树了
# coding：utf-8
L = list(input())

def ifRight(L):
    root = L[-1]
    del L[-1]
    leftTree = []
    rightTree = []
    splitIndex = -1
    for i in range(len(L)):
        if L[i]< root:
            leftTree.append(L[i])
            splitIndex = i
        else:
            break
    for i in range(splitIndex+1,len(L)):
        if L[i]> root:
            rightTree.append(L[i])
        else:
            return False#这里之所以不同主要是因为当右子树有小于根节点的节点时，即可判断该二叉树不是二叉搜索树
    if len(leftTree)<=1:
        left = True
    else:
        left = ifRight(leftTree)#此处用递归来判断左子树是否仍然符合二叉搜索的定义
    if len(rightTree)<=1:
        right = True
    else:
        right = ifRight(rightTree)
    return (right and left)

ifRight(L)


# In[106]:

#a,b,c,d 四个数字算24点 如果可以成立则输出1，不可以输出0

