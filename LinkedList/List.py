'''
Created on Jul 10, 2018

@author: MOHIT
'''
from LinkedList.Node import Node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def set_head(self, value):
        self.__head = value

    def set_tail(self, value):
        self.__tail = value

    def display_linkedlist(self):
        temp = self.get_head()
        while temp!=None:
            print(temp.get_data(), end=" ")
            temp=temp.get_next()
   
    def length_linkedlist(self):
        temp=self.get_head()
        i=0
        while temp!=None:
            i+=1
            temp=temp.get_next()   
        return i 
    
    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.get_head()==None and self.get_tail()==None:
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            new_node.set_next(self.get_head())
            self.set_head(new_node)
            
    def insert_at_middle(self,pos,data):
        if pos<1:
            print("Position does not exist")
            return None
        else:
            if pos==1:
                self.insert_at_begining(data)
            elif pos==self.length_linkedlist()+1:
                self.insert_at_end(data)    
            elif pos>self.length_linkedlist()+1:
                print("Position does not exist")     
            else:
                new_node = Node(data)
                temp=self.get_head()
                i=1
                while i<pos-1:
                    temp=temp.get_next()
                    i+=1    
                new_node.set_next(temp.get_next())
                temp.set_next(new_node)            
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.get_head()==None and self.get_tail()==None:
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            self.get_tail().set_next(new_node)
            self.set_tail(new_node) 
            
    def del_at_begin(self):
        if self.length_linkedlist()==0:
            print("The list is empty")
        else:
            self.set_head(self.get_head().get_next()) 
                                  
    def del_at_end(self):
        if self.length_linkedlist()==0:
            print("List is empty")
        elif self.length_linkedlist()==1:
            self.set_head(None)
            self.set_tail(None)
        else:
            i=1
            temp=self.get_head()
            while i<self.length_linkedlist()-1:
                temp=temp.get_next()
                i+=1    
            temp.set_next(None)
            self.set_tail(temp)
            
    def del_at_pos(self,pos):
        if self.length_linkedlist()==0:
            print("List is empty")
            return                     
        if pos<1 or pos>self.length_linkedlist():
            print("Position does not exist")
        else:
            if pos==1:
                self.set_head(self.get_head().get_next())
            elif pos == self.length_linkedlist():
                self.del_at_end()   
            else:
                i=1
                temp=self.get_head()    
                while i<pos-1:
                    temp=temp.get_next()
                    i+=1
                temp.set_next(temp.get_next().get_next())    
    
    def del_using_data(self,data):
        if self.length_linkedlist()==0:
            print("List is empty")
            return        
        else:
            prev = self.get_head()
            now = self.get_head()
            if self.length_linkedlist()==1 and now.get_data()==data:
                self.set_head(None)
                self.set_tail(None)    
            else:
                while True:
                    if now.get_data()==data:
                        if now==self.get_head():
                            self.set_head(now.get_next())
                            break
                        elif now==self.get_tail():
                            self.set_tail(prev)
                            prev.set_next(None)
                            break
                        else:
                            prev.set_next(now.get_next())
                            break
                    prev=now
                    now=now.get_next()        
                
                
list1 = LinkedList()
list1.insert_at_middle(1, "Mohit")
list1.insert_at_middle(2,"Kansha")
list1.insert_at_middle(3,"Prachi")
list1.insert_at_middle(4, "Mohit")
# list1.insert_at_begining("Himanshi")
# list1.insert_at_middle(2, "Mohit")
print("Head: ",list1.get_head())
print("Tail: ",list1.get_tail())

list1.display_linkedlist()     
print("\n"+"Length of linked list is: ",list1.length_linkedlist())

          
