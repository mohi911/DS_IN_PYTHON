'''
Created on Jul 29, 2018

@author: MOHIT
'''
from DS.LinkedList.Node import Node

class list_block:
    count=1
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__next=None
        self.__nodeCount=0
        self.__blockNumber=list_block.count
        list_block.count+=1

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value

    def get_block_number(self):
        return self.__blockNumber

    def set_block_number(self, value):
        self.__blockNumber = value

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def get_node_count(self):
        return self.__nodeCount

    def set_head(self, value):
        self.__head = value

    def set_tail(self, value):
        self.__tail = value

    def set_node_count(self, value):
        self.__nodeCOunt = value
    
   
class Unrolled_list():
    
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
        if self.get_head()==None:
            return 0
        else:
            i=1
            block=self.get_head()
            while block==None:
                temp=block.get_head()
                temp=temp.get_next()
                while temp is not self.get_head():
                    i+=1
                    temp = temp.get_next()      
            block=block.get_next()
            return i
    
    def display_list(self):
        if self.get_head()==None:
            return "List is empty"  
        else:
            block=self.get_head()
            print("hi1")
            while block!=None:
                print("The block number is : ",block.get_block_number())
                temp=block.get_head()
                print(temp.get_data(),end=" ")
                temp =temp.get_next()
                while temp is not self.get_head():
                    print(temp.get_data(),end=" ")
                    temp=temp.get_next()
                block=block.get_next()
                
    def total_block_number(self):
        if self.get_head()==None:return 0
        else:
            block=self.get_head()
            i=0
            while block!=None:
                i+=1
                block=block.get_next()
            return i
    
    def add_element(self,blockNumber,data):
        if(self.get_head()==None):
            blockHead=list_block()
            new_node=Node(data)
            self.set_head(blockHead)
            blockHead.set_head(new_node)
            blockHead.set_tail(new_node)
            blockHead.get_head().set_next(new_node)
            blockHead.set_node_count(blockHead.get_node_count()+1)   
            
            
list1=Unrolled_list()
list1.add_element(0,"Mohit")   
list1.display_list()         
                     
        