class Node:
    def __init__(self, data):
        self.__data = data
        self.__pointer = -1
    def getData(self):
        return self.__data
    def getPointer(self):
        return self.__pointer
    def setData(self, data):
        self.__data = data
    def setPointer(self, ptr):
        self.__pointer = ptr

class stack:
    def __init__(self, size=5):
        self.__stackData = [Node("") for i in range(size)]
        for i in range(len(self.__stackData)-1):
            self.__stackData[i].setPointer(i+1)
        self.__top = -1
        self.__maxSize = size
        self.__nextFree = 0

    def isEmpty(self):
        return self.__top == -1
    def pop(self):
        if self.isEmpty():
            print('stack is empty')
        else:
            poppedItem = self.__stackData[self.__top].getData()
            temp = self.__top
            self.__top = self.__stackData[self.__top].getPointer()
            self.__stackData[temp].setPointer(self.__nextFree)
            self.__nextFree = temp
            return poppedItem

    def isFull(self):
        return self.__top == self.__maxSize-1
        
    def push(self, item):
        if self.isFull():
            print('stack is full')
        else:
            self.__stackData[self.__nextFree].setData(item)
            temp = self.__top
            self.__top = self.__nextFree
            self.__nextFree = self.__stackData[self.__nextFree].getPointer()
            self.__stackData[self.__top].setPointer(temp)

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            item = self.__stackData[self.__top].getData()
            return item
        
            
        
