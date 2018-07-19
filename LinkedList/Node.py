'''
Created on Jul 10, 2018

@author: MOHIT
'''
class Node:
    
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, value):
        self.__data = value

    def set_next(self, value):
        self.__next = value


    def has_next(self):
        return self.__next!=None
     
    def __str__(self):
        return "The data in this node is: "+ str(self.get_data())    