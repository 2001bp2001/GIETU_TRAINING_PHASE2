#linked-list
class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class slinkedlist:
    def __init__(self):
        self.headval=None
        
    # trversal of linked list
    def listprint(self):
        printval=self.headval
        while printval is   not None:
            print(printval.dataval)
            printval=printval.nextval
            
    # add new node at begning
    def at_begning(self,data):
        new_node=node(data)
        #update the new node next val to existing node
        new_node.nextval=self.headval
        self.headval= new_node

     #at end addition   
    def atend(self,data):
        newnode=node(data)
        if self.headval==None:
            self.headval=newnode
        else:
            laste=self.headval
            while(laste.nextval):
                laste=laste.nextval
            laste.nextval=newnode
            
    #in between insert
    def between(self,mid_node,data):
        newnode= node(data)
        if mid_node==None:
            print("node not present")
        else:
            newnode= node(data)
            newnode.nextval=mid_node.nextval
            mid_node.nextval=newnode
            
    #deletion from start       
    def delete_start(self):
        if self.headval is None:
            print(" the element need to delet is not there")
            return
        self.headval=self.headval.nextval
    #deletion from end
    def delete_end(self):
        if self.headval is None:
            print(" the element need is not there")
            return
        last=self.headval
        while( last.nextval.nextval is not None):
            last=last.nextval
        last.nextval=None
        
    #deletion through value:
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
    #search_item
    def search_item(self,x):
        if self.headval is None:
            print("list has no element")
        n=self.headval
        while n is not None:
            if n.dataval==x:
                print("item found")
                return True
            n=n.nextval
        print("item not found")
        return False
    #insert at a index
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
            
    #count no of nodes
    def get_count(self):
        if self.headval is None:
            return 0
        count=0
        n=self.headval
        while n is not None:
            count+=1
            n=n.nextval
        return count            
            
list1=slinkedlist()
list1.headval=node("mon")
e2=node("tue")
e3=node("wed")
#link first node linked to second
list1.headval.nextval=e2
e2.nextval=e3
list1.at_begning("sun")
list1.atend("fri")
list1.between(list1.headval.nextval.nextval,"thus")
'''list1.listprint()
print("after deletion")
list1.delete_start()
list1.listprint()
list1.delete_end()
list1.delete_mid(list1.headval.nextval.nextval)
list1.delete_value("")
list1.search_item("fri")'''
list1.insert_value_by_index(3,"hi")
print(list1.get_count())
list1.listprint()
