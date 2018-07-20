'''
Created on Jul 19, 2018

@author: MOHIT
'''
from DS.LinkedList.Node import Node
class CircularList:
    
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

    
    def length_list(self):
        temp= self.get_head()
        if self.get_head()==None:
            return 0
        else:
            i=1
            temp=temp.get_next()
            while temp is not self.get_head():
                i+=1
                temp = temp.get_next()      
            return i 
              
    def display_list(self):
        if self.length_list()==0:
            print("List is empty")
        else:
            temp = self.get_head()
            print(temp.get_data(),end=" ")
            temp =temp.get_next()
            while temp is not self.get_head():
                print(temp.get_data(),end=" ")
                temp=temp.get_next()
                
    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.length_list()==0:
            self.set_head(new_node) 
            self.set_tail(new_node) 
            self.get_tail().set_next(self.get_head())
        else:
            self.get_tail().set_next(new_node)
            new_node.set_next(self.get_head())       
            self.set_head(new_node)
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.length_list()==0:
            self.set_head(new_node) 
            self.set_tail(new_node) 
            self.get_tail().set_next(self.get_head())
        else:
            self.get_tail().set_next(new_node)
            new_node.set_next(self.get_head())       
            self.set_tail(new_node)        
            
    def insert_at_pos(self,pos,data):
        new_node = Node(data)
        if pos<1 or pos>self.length_list()+1:
            print("Invalid position")
            return
        elif pos==1:
            self.insert_at_begining(data)
        elif pos==self.length_list()+1:
            self.insert_at_end(data)
        else:
            i=1
            temp=self.get_head()
            while i<pos-1:
                temp=temp.get_next()
                i+=1
            new_node.set_next(temp.get_next())
            temp.set_next(new_node)   
               
list1 = CircularList()
list1.insert_at_begining("Mohit")
list1.insert_at_end("Kansha")
list1.insert_at_begining("Prachi")
list1.insert_at_pos(0,"Himanshi")
list1.display_list()
print("\nLength of list is :",list1.length_list())
print("Head: ",list1.get_head())
print("Tail: ",list1.get_tail())



