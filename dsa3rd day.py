   #DSA#-ASSGN -3
'''
Given two list ,both having integer element ,write a python program using python lists to create and return a new list as per the rule given below:
if double of an element in list1 is present in list2,
then add it to the new list.
estimate time :20 minutes
sample input
list1-[11,8,23,7,25,15]
list2-[6,33,50,31,46,78,16,34]
expected output
new_list-[8,23,25]
'''
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
list3=[]
for i in list1:
    for j in list2:
        if i*2==j:
            list3.append(i)
print(list3)

#*************************************************************************************************************************************

'''
a teacher has given a project assignment to a class of 10 students.
she wants to store the marks (out of 100) scored by each student.the marks scored are as mentioned below:
89,78,99,76,77,67,99,98,90
write a python program to store the marks in a list and perform the following:
    1.the teacher forgot to include the marks of one student.Insert 78 at index position, 8 and display the marks of all 10 students.
    2.the teacher also wants to know the scored  by students represented by index position, 5 and 7.identify and display the two marks.
    '''
class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class student:
    def __init__(self):
        self.headval=None
        
    # trversal of linked list
    def listprint(self):
        printval=self.headval
        while printval is   not None:
            print(printval.dataval)
            printval=printval.nextval
            
    def insert_value_by_index(self,index,data):
        if index==1:
            new_node=node(data)
            new_node.nextval=self.headval
            self.headval=new_node
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.nextval
            i+=1
        if n is None:
            print("index out of bound")
        else:
            new_node=node(data)
            new_node.nextval=n.nextval
            n.nextval=new_node
    def search(self,index):
        if index==1:
            print(self.headval.dataval)
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.nextval
            i+=1
        if n is None:
            print("index out of bound")
        else:
            print(n.nextval.dataval)
        
        
            
list1=student()
list1.headval=node(89)
e2=node(78)
e3=node(99)
e4=node(76)
e5=node(77)
e6=node(67)
e7=node(99)
e8=node(98)
e9=node(90)
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
list1.insert_value_by_index(8,78)
list1.listprint()
print()
list1.search(5)
print()
list1.search(7)

#*****************************************************************************************************************************************
#question
''' character given in the linked listas per the rules given below
replace '*' or '/'by single space
in case of two consecutive '*' or '/'replace those those two consecutive to single space andthe nest charater to upper case
assume that there will not be more than two consecutiveoccurance of '*' or '/' '''

class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class student:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval,end='')
            printval=printval.nextval
    
    def delete_value(self,data):
        if self.headval is None:
            print("no node to delete")
            return
        if self.headval.dataval==data:
            self.headval=self.headval.nextval
            return
        n=self.headval
        while(n.nextval is not None):
            if n.nextval.dataval==data:
                break 
            n=n.nextval
        if n.nextval is None:
            print(" item not found")
        else:
            n.nextval=n.nextval.nextval
                    
def new_list(list1):
        l1=[]
        if list1.headval is None:
            print(" no element in list")
        if list1.headval.nextval is None:
            l1.append(list1.head.dataval)
            return
        n=list1.headval
        while n.nextval is not None:
            l1.append(n.nextval.dataval)
            n=n.nextval
        
        for i in range(len(l1)):
            if( l1[i]=='*' or l1[i]=='/'):
                l1[i]=' '
            elif l1[i-1]==' ' and l1[i-2]==' ':
                print('hi')
                l1[i-1]=''
                l1[i]=l1[i].upper()
            else:
                continue
        for i in l1:
            print(i,end='')        
                    
list1=student()
list1.headval=node('A')
e2=node('n')
e3=node('*')
e4=node('/')
e5=node('a')
e6=node('p')
e7=node('p')
e8=node('l')
e9=node('e')
e10=node('*')
e11=node('a')
e12=node('/')
e13=node('day')
e14=node('*')
e15=node('*')
e16=node('k')
e17=node('e')
e18=node('e')
e19=node('p')
e20=node('s')
e21=node('/')
e22=node('*')
e23=node('a')
e24=node('/')
e25=node('/')
e26=node('d')
e27=node('o')
e28=node('c')
e29=node('t')
e30=node('o')
e31=node('r')
e32=node('*')
e33=node('A')
e34=node('w')
e35=node('a')
e36=node('y')
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
e9.nextval=e10
e10.nextval=e11
e11.nextval=e12
e12.nextval=e13
e13.nextval=e14
e14.nextval=e15
e15.nextval=e16
e16.nextval=e17
e17.nextval=e18
e18.nextval=e19
e19.nextval=e20
e20.nextval=e21
e21.nextval=e22
e22.nextval=e23
e23.nextval=e24
e24.nextval=e25
e25.nextval=e26
e26.nextval=e27
e27.nextval=e28
e28.nextval=e29
e29.nextval=e30
e30.nextval=e31
e31.nextval=e32
e32.nextval=e33
e33.nextval=e34
e34.nextval=e35
e35.nextval=e36
new_list(list1)'''



#************************************************************************************************************************************

'''class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class slinkedlist:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        printval=self.headval
        while printval is   not None:
            print(printval.dataval)
            printval=printval.nextval
#reverse of list
    def rev(self):
        prev=None
        current=self.headval
        while(current is not None):
            nextval=current.nextval
            current.nextval=prev
            prev=current
            current=nextval
        self.headval  =prev
list1=slinkedlist()
list1.headval=node("mon")
e2=node("tue")
e3=node("wed")
list1.headval.nextval=e2
e2.nextval=e3
list1.listprint()
print()
list1.rev()
list1.listprint()
#*****************************************************************************************************************************************
#double linked-list
class node:
    def __init__(self,dataval):
        self.prev=None
        self.data=dataval
        self.next=None
class dlinkedlist:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def at_beg(self,value):
        new_node=node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def at_end(self,value):
        new_node=node(value)
        if self.isEmpty():
            self.at_beg(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def  printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=' ')
            temp=temp.next
    def insertAtPosition(self,value,position):
            temp = self.head
            count = 1 
            while temp is not None:
                if count == position - 1:
                    break
                count +=1 
                temp = temp.next
            if position == 1:
                 self.insertAtBeginning(value)
            elif temp is None:
                print("There are less than {}-1 elements in the linked list".format(position,position))
            elif temp.next is None:
                self.insertAtEnd(value)
            else:
                new_node = node(value)
                new_node.next = temp.next
                new_node.previous = temp
                temp.next.previous = new_node
                temp.next= new_node
            
    def delete_beg(self):
        if self.isEmpty():
            print("linked list is empty cannot delete")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def delete_end(self):
        if self.isEmpty():
            print("linked list is empty cannot delete")
        elif  self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            temp.prev=None
    def del_posn(self,posn):
        if self.isEmpty:
            print("linked list is empty.cannot delete elements")
        elif posn==1:
            self.delete_start()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==posn:
                    break
                temp=temp.next
                count+=1
            if temp is None:
               print("there is no element to print")
            elif temp.next is None:
                self.delete_last()
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
        
    
x=dlinkedlist()
print(x.isEmpty())
x.at_end(5)
x.printlist()
x.at_end(15)
x.at_end(20)
x.at_end(25)
print()
x.printlist()
print()
print(x.length())
print()
x.insertAtPosition(2,2)
x.delete_beg()
x.delete_end()
x.del_posn(1)
x.printlist()

#************************************************************************************************************************************* 
#evalution of  postfix
class evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.array[-1]
    def push(self,data):
        self.top+=1
        self.array.append(data)
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return '$'
    def evaluation(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))

        return int(self.pop())
if __name__=='__main__':
    exp="231*+9-"
    obj=evaluate(len(exp))
    print("evalution ",obj.evaluation(exp))
#********************************************************************************************************************************
      
    
            
    

            



