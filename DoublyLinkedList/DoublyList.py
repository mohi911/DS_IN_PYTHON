'''
Created on Jul 14, 2018

@author: MOHIT
'''
from LinkedList.DoublyNode import DoublyNode
class DoublyList():
    def __init__(self,head=None,tail=None):
        self.__head=head
        self.__tail=tail

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def set_head(self, value):
        self.__head = value

    def set_tail(self, value):
        self.__tail = value

    def display_linkedlist_forward(self):
        temp = self.get_head()
        while temp!=None:
            print(temp.get_data(), end=" ")
            temp=temp.get_next()
    
    def display_linkedlist_backward(self):
        temp=self.get_tail()
        while temp!=None:
            print(temp.get_data(), end=" ")
            temp=temp.get_prev()        
   
    def length_linkedlist(self):
        temp=self.get_head()
        i=0
        while temp!=None:
            i+=1
            temp=temp.get_next()   
        return i 
    
    def insert_at_begining(self,data):
        new_node = DoublyNode(data)
        if self.length_linkedlist()==0:
            self.set_head(new_node)
            self.set_tail(new_node) 
        else:
            new_node.set_next(self.get_head())
            self.get_head().set_prev(new_node)
            self.set_head(new_node)
                  
    def insert_at_end(self,data):
        new_node = DoublyNode(data)
        if self.length_linkedlist()==0:
            self.set_head(new_node)
            self.set_tail(new_node) 
        else:
            i=1
            temp=self.get_head()
            while i<self.length_linkedlist():
                temp = temp.get_next()
                i+=1
            temp.set_next(new_node)
            new_node.set_prev(temp)
            self.set_tail(new_node) 
    
    def insert_at_pos(self,pos,data):
        if pos<1 or pos>self.length_linkedlist()+1:
            print("Position does not exist")
            return
        elif pos==1:
            self.insert_at_begining(data)
        elif pos==self.length_linkedlist()+1:
            self.insert_at_end(data) 
        else:
            i=1
            new_node=DoublyNode(data)
            temp=self.get_head()
            while i<pos:
                temp = temp.get_next()
                i+=1
            new_node.set_next(temp)
            new_node.set_prev(temp.get_prev())                                  
            temp.get_prev().set_next(new_node)
            temp.set_prev(new_node)
            
    def del_at_begining(self):
        if self.length_linkedlist()==0:
            print("List is empty")
            return
        elif self.length_linkedlist()==1:
            self.set_head(None)
            self.set_tail(None)
        else:
            self.set_head(self.get_head().get_next())
            self.get_head().get_prev().set_next(None)
            self.get_head().set_prev(None)          
            
    def del_at_end(self):
        if self.length_linkedlist()==0:
            print("List is empty")
            return
        elif self.length_linkedlist()==1:
            self.set_head(None)
            self.set_tail(None)
        else:
            temp = self.get_tail()
            self.set_tail(temp.get_prev())
            self.get_tail().set_next(None)
            temp.set_prev(None)
            
    def del_at_pos(self,pos):
        if pos<1 or pos>self.length_linkedlist():
            print("Position does not exist")
            return
        elif pos==1:
            self.del_at_begining()
        elif pos==self.length_linkedlist():
            self.del_at_end()
        else:
            i=1
            temp = self.get_head()
            while i<pos:
                temp = temp.get_next()
                i+=1
            temp.get_prev().set_next(temp.get_next())
            temp.get_next().set_prev(temp.get_prev())
            temp.set_next(None)
            temp.set_prev(None)        
    
    def del_using_data(self,data):                
        if self.length_linkedlist()==0:
            print("Position does not exist")
            return
        else:
            temp=self.get_head()
            while temp!=None:
                if temp.get_data()==data:
                    if temp.get_prev()!=None:
                        if temp.get_next()==None:
                            self.set_tail(temp.get_prev())
                            self.get_tail().set_next(None)
                            temp.set_prev(None)
                            return
                        else:
                            temp.get_prev().set_next(temp.get_next())
                            temp.get_next().set_prev(temp.get_prev())
                            temp.set_next(None)
                            temp.set_prev(None)
                            return 
                    else:
                        if temp.get_next()==None:
                            self.set_head(None)
                            self.set_tail(None)
                            return
                        else:
                            self.set_head(temp.get_next())
                            temp.get_next().set_prev(None)
                            temp.set_next(None)
                            return
                else:
                    temp=temp.get_next()
            
list1 = DoublyList()
list1.insert_at_end("Mohit")
list1.insert_at_end("Kansha")
list1.insert_at_end("Prachi")
list1.insert_at_end("Himanshi")

print("Head: ",list1.get_head())
print("Tail: ",list1.get_tail())
list1.display_linkedlist_forward()
print("\n")
list1.display_linkedlist_backward()
print("\nLength of linked list is: "+ str(list1.length_linkedlist()))                     

