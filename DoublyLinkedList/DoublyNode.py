'''
Created on Jul 14, 2018

@author: MOHIT
'''
class DoublyNode():
    
    def __init__(self,data,prev=None,after=None):
        self.__data=data
        self.__prev=prev 
        self.__after=after

    def get_data(self):
        return self.__data


    def get_prev(self):
        return self.__prev


    def get_next(self):
        return self.__after


    def set_data(self, value):
        self.__data = value


    def set_prev(self, value):
        self.__prev = value


    def set_next(self, value):
        self.__after = value

    def __str__(self):
        return "The data in the node is: "+str(self.get_data())    
        
        