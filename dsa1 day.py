'''#stack is linear data structure(lifo)
class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*max_size#[None,None,None,None]
        self.__top=-1

    def is_full(self):
        if self.__top==self.__max_size-1:
             return True
        return False
        
    def is_empty(self):
        if self.__top==-1:
              return True
        return False
        
    def push(self,data):
        if self.is_full():
               print("the stack is full")
        else:
            self.__top+=1
            self.__element[self.__top]=data
            
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            data=self.__element[self.__top]
            self.top-=1
            return data
            
    def display(self):
        if self.is_empty():
             print("stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index-=1
                
    def get_max_size(self):
        return self.__max_size
ball_stack=stack(4)
print("is stack empty",ball_stack.is_empty())
ball_stack.push(5)
print("is stack empty",ball_stack.is_empty())
ball_stack=stack(6)
ball_stack=stack(7)
ball_stack=stack(8)
ball_stack.display()
print("size of the stack",ball_stack.get_max_size())
print(" the element deleted",ball_stack.pop())
print("after deleting the element")
ball_stack.display()
print("size of stack",ball_stack.get_max_size())'''


#Queue linear data structure
'''class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*max_size#[None,None,None,None]
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("queue if full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
                
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])
               
    def get_max_size(self):
        return self.__max_size
queue1=queue(10)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())

queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("element dleted",queue1.dequeue())
queue1.display()'''

#question1
'''given a queue of whole numbers.write a python function to return a new queue which contains the evenly divisible number
note:- a no is said to be evenly divisible by all the number in the given range without any reminder.consider the range to be form
1 to 10(both inclusive)
assume that there will always the few elements in the input queue,which are divisible by the number in the mention range
example:
input queue: 13983,10080,7113,2520,2500(front-rear)
output queue: 10080,2520(fornt-rear)'''
'''class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*max_size#[None,None,None,None]
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("queue if full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])

     def get_max_size(self):
        return self.__max_size
            
def find(queue1):
    new_queue=Queue(5)
    while(not queue1.is_empty()):
        count=0
        ele=queue1.dequeue()
        for i in range(1,11):
            if ele%i!=0:
                count=1
                break
        if count==0:
            new_queue.enqueue(ele)
    return new_queue

queue1=Queue(5)
queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)
queue1.display()
find(queue1).display()'''  

#question 2
'''Given two lists,both having string elements, write a python program using python
program using python lists to create a new string as per the rule given below:
the first element in list1 should be merged with last element in list2,second element
in list1 should be merged with second last element in list2 and so on.if an element
in list1/list2 in None ,then the corresponding element in the other list should be kept
as it is in the merged list.'''
'''l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
for i in range(len(l1)):
    if l1[i]!=None and l2[-(i+1)]!=None:
        print( l1[i]+l2[-(i+1)],end=' ')
    elif l1[i]==None:
        print(l2[-(i+1)],end=' ')
    else:
        print( l1[i],end=' ')'''
#question 3
'''Given two queues, one integer queue and another character queue,
Write a python program to merge then to form a sigle queue.
Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queue has more elements than the other, add all the additional
elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues.

For example,
Input-- queue1:3,6,8 queue2:b,y,u,t,r,o
Output-- 3,b,6,y,8,u,t,r,o '''
'''class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*max_size#[None,None,None,None]
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            print("queue if full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
            
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])

    def get_max_size(self):
        return self.__max_size
               
    
def conn(queue1,queue2):
    size=0
    l1=[]
    i=0
    if queue1.get_max_size()>queue2.get_max_size():
        size=queue1.get_max_size()
    else:
        size=queue2.get_max_size()
    while(i<size):
        if i<queue1.get_max_size():
            ele=str((queue1.dequeue()))
            l1.append(ele)
        if i<queue2.get_max_size():
            ele=str((queue2.dequeue()))
            l1.append(ele)
        i+=1
        print(','.join(l1))
            
queue1=queue(3)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2=queue(6)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')
conn(queue1,queue2)'''


        
        



        

        

        

        
        



    
                
                




    












        
            
        

        
