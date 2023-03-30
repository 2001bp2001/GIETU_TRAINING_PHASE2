
'''
11.A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment.
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:

count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.
'''
class compartment:
    def __init__(self,name,total_seats,no_passengers):
        self.next=None
        self.name=name
        self.t_seats=total_seats
        self.no_passengers=no_passengers
class linkedlist:
    def __init__(self,tname):
        self.head=None
        self.name=tname
    def count_comp(self):
        if self.head is None:
            return 0
            print("no compartment")
        n=self.head
        count=0
        while n is not None:
            n=n.next
            count+=1
        return count
    def listprint(self):
        printval=self.head
        while printval is   not None:
            print(printval.name,end=' ')
            print(printval.t_seats,end=' ')
            print(printval.no_passengers,end=' ')
            print()
            printval=printval.next
    def vacancy(self):
        if self.head is None:
            return 0
            print("no compartment")
        count=0
        n=self.head
        while n is not None:
            x=(((n.t_seats-n.no_passengers)*100)/n.t_seats)
            if x>50:
                count+=1
            n=n.next
        return count
class train:
    def __init__(self,tname,comp_list):
        self.__tname=tname
        self.__comp_list=comp_list
    def get_name(self):
        return self.__tname
    def get_comp_list(self):
        return self.__comp_list
                      
list1=linkedlist("basanti")
list1.head=compartment("sl",150,30)
comp2=compartment("s2",150,60)
comp3=compartment("s2",150,90)
comp4=compartment("s2",150,10)
comp5=compartment("s2",150,80)
list1.head.next=comp2
comp2.next=comp3
comp3.next=comp4
comp4.next=comp5
list1.listprint()
print("number of compartment=",list1.count_comp())
print("no of compartment having vacanvcy more than 50%=",list1.vacancy())
t=train("basanti",list1)
