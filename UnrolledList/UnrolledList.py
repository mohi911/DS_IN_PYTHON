'''
Created on Jul 29, 2018

@author: MOHIT
'''
from DSpython.LinkedList.LinkedList.Node import Node




class list_block:
    count = 1

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__next = None
        self.__nodeCount = 0
        self.__blockNumber = list_block.count
        list_block.count += 1

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
        self.__nodeCount = value


class Unrolled_list():
    
    __blockSize=2
    
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def set_head(self, value):
        self.__head = value

    def set_tail(self, value):
        self.__tail = value

    def length_list(self):
        if self.get_head() is None:
            return 0
        else:
            i = 0
            block = self.get_head()
            while block is not None:
                temp = block.get_head()
                while temp.get_next() is not block.get_head():
                    i += 1
                    temp = temp.get_next()
                i+=1           
                block = block.get_next()
            return i

    def display_list(self):
        if self.get_head() is None:
            return "List is empty"
        else:
            block = self.get_head()
            while block is not None:
                print("\nThe block number is : ", block.get_block_number())
                temp = block.get_head()
                print(temp.get_data(), end=" ")
                temp = temp.get_next()
                while temp is not block.get_head():
                    print(temp.get_data(), end=" ")
                    temp = temp.get_next()
                block = block.get_next()

    def total_block_number(self):
        if self.get_head() is None:
            return 0
        else:
            block = self.get_head()
            i = 0
            while block is not None:
                i += 1
                block = block.get_next()
            return i

    def add_element(self, blockNumber, data):
        if(self.get_head() is None):
            blockHead = list_block()
            new_node = Node(data)
            self.set_head(blockHead)
            blockHead.set_head(new_node)
            blockHead.set_tail(new_node)
            blockHead.get_head().set_next(new_node)
            blockHead.set_node_count(blockHead.get_node_count()+1)
        else:
            if blockNumber == 1:
                block = self.get_head()
                new_node = Node(data)
                block.get_tail().set_next(new_node)
                new_node.set_next(block.get_head())
                block.set_head(new_node)
                block.set_node_count(block.get_node_count()+1)
                self.shift()
            elif blockNumber>self.total_block_number():
                print("blockNumber exceeds the actual number of blocks")
                return
            else:
                i=1
                block = self.get_head()
                new_node = Node(data)
                while i is not blockNumber:
                    block=block.get_next()
                    i+=1
                temp=block.get_tail()
                temp.set_next(new_node)
                new_node.set_next(block.get_head())
                block.set_head(new_node)
                block.set_node_count(block.get_node_count()+1)
                self.shift()
                         
    def shift(self):
        block = self.get_head()
        while block is not None:
            while block.get_node_count()>Unrolled_list.__blockSize:
                temp = block.get_head()
                shift_node = block.get_tail()
                while temp.get_next() is not block.get_tail():
                    temp = temp.get_next()           
                temp.set_next(block.get_head())
                block.set_tail(temp)
                if block.get_next()==None:
                    new_block = list_block()
                    block.set_next(new_block)
                    new_block.set_head(shift_node)
                    new_block.set_tail(shift_node)
                    new_block.get_tail().set_next(new_block.get_head())
                    block.set_node_count(block.get_node_count()-1)
                    new_block.set_node_count(new_block.get_node_count()+1)
                else:
                    next_block= block.get_next()
                    next_block.get_tail().set_next(shift_node)
                    shift_node.set_next(next_block.get_head())
                    next_block.set_head(shift_node)
                    block.set_node_count(block.get_node_count()-1)
                    next_block.set_node_count(next_block.get_node_count()+1)
            block = block.get_next()         
    
    def get_element(self,k):
        if k<=0 or k>self.length_list():
            return "Invalid index"
        else:
            j = (k+1)//Unrolled_list.__blockSize  #item exist in block j
            m = k - (Unrolled_list.__blockSize*(j-1))  #mth item is required in jth block
            l=1
            block = self.get_head()
            while l<j:
                block = block.get_next()
                l+=1
            x=1
            temp = block.get_head() 
            while x<m:
                temp = temp.get_next()
                x+=1
            return temp    
               
                
            
            
            
