'''write a python program to remove all duplicate elements from a sorted list containing integer data
use the linkedlist class and methoda in it to implement the above program
example:
input linkedlist: 10 10 20 20 30 30 30 40 50
output linkedlist 10 20 30 40 50
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def display(self):
        printval=self.head
        while printval is   not None:
            print(printval.data,end=' ')
            printval=printval.next
            
    def atend(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            laste=self.head
            while(laste.next):
                laste=laste.next
            laste.next=newnode
    def at_beg(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head= new_node

def new_list(list1,list2):
    l1=[]
    l2=[]
    n=list1.head
    while n.next is not None:
        ele=n.next.data
        l1.append(ele)
        n=n.next
    
    for i in l1:
        if i not in l2:
            l2.append(i)
    for i in l2:
        list2.atend(i)
    list2.display()
        
        
list1=linkedlist()
list2=linkedlist()
list1.head=node(10)
e2=node(10)
e3=node(20)
e4=node(20)
e5=node(30)
e6=node(30)
e7=node(30)
e8=node(40)
e9=node(50)
list1.head.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
e5.next=e6
e6.next=e7
e7.next=e8
e8.next=e9
new_list(list1,list2)
#***************************************************************************************************************************************
'''given a stack of integer write a python program that update update the input stack such that the occurancve of smallest values
are at the of the stack,while the order of the other elements remains the same
for example:-
input stack:5 66 5 8 7
output: 66 8 7 5 5
'''
class sort:
    def __init__(self):
        self.top=-1
        self.stack=[]
    def isEmpty(self):
        return True if self.top==-1 else False
    #def display():
        
    def push(self,data):
        self.top+=1
        self.stack.append(data)
        
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
        else:
            return 'no'
    def sorted(self):
        l1=[]
        while self.top!=-1:
            l1.append(self.pop())
        l1.sort()
        for i in l1:
            self.push(i)
    def display(self):
        if self.isEmpty():
             print("stack is empty")
        else:
            index=self.top
            while(index>=0):
                print(self.stack[index])
                index-=1
obj=sort()
obj.push(5)
obj.push(66)
obj.push(5)
obj.push(8)
obj.push(7)
obj.sorted()
obj.display()
#***********************************************************************************************************************************************
#linear search in python
def linearsearch(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=2
n=len(array)
result=linearsearch(array,n,x)
if result==-1:
    print("element not found")
else:
    print("element found at index=",result)
#****************************************************************************************************************************************
#binary search
def binarysearch(array,x,low,high):
    while(low<=high):
        mid=high+low//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=9
x=14
x=4
result=binarysearch(array,x,0,len(array)-1)
if result==-1:
    print("element not found")
else:
    print("elemnt index=",result)
#**************************************************************************************************************************************
#binary tree traversal
class node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):#left-root-right
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end="")
        inorder(root.right)
def preorder(root): #root-left-right
    if root:
        print(str(root.val)+"->",end="")
        preorder(root.left)
        preorder(root.right)
def postorder(root):#left-right-root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end="")
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("inorder traversal")
inorder(root)
print("\npreorder traversal")
preorder(root)
print("\npostorder traversal")
postorder(root)

#*********************************************************************************************************************************
#insertion of node in birany search tree
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.key=item
def inorder(root):#left-root-right
    if root:
        inorder(root.left)
        print(str(root.key)+"->",end="")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("inorder travesal:",end='')
inorder(root)

#**********************************************************************************************************************************
#question
'''Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. The task is to 
find the unknown words (other than the words they already know) from the given text. Write a python function which 
accepts the text and the known list of words and returnsthe set of unknown words found.Return -1 if there are no unknown words.


Sample Input	
Text: "the sun rises in the east"
Vocabulary: ["sun","in","east","doctor","day"]	
Expected Output
{'rises', 'the'}'''

l2=["sun","in","east","doctor","day"]
n=list(map(str,input().split()))
l3=[]
l4=[]
n=list(set(n))
for i in n:
    if i not in  l2:
        l3.append(i)
print(set(sorted(l3)))


       
           





      
    
