#Normal queue in using Linked List
#20S24

class Node:
    def __init__(self, data, pointer = -1):
        self.__data = data
        self.__pointer = pointer

#default accessor and modifier
    def setData(self, data):
        self.__data = data
    def getData(self):
        return self.__data

    def setPointer(self, pointer):
        self.__pointer = pointer
    def getPointer(self):
        return self.__pointer

class queue:
    def __init__(self, size = 3):
        self.__queue = [Node(None) for i in range(size)]
        self.__front = -1
        self.__nextfree = 0
        self.__limit = size
        self.__size = 0

    def isFull(self):
        return self.__limit == self.__size

    def isEmpty(self):
        return self.__size == 0

    def enqueue(self, data):
        if self.isFull():
            print('queue is full')
            return
        self.__queue[self.__nextfree].setData(data)
        if self.__front == -1:
            temp = self.__queue[self.__nextfree].getPointer()
            self.__queue[self.__nextfree].setPointer(-1)
            self.__front = self.__nextfree
            self.__nextfree = temp
            self.__size += 1
        else:
            current = self.__front
            while current != self.__size:
                


    def display(self):
        print('Start =', self.__Start, '\nNextfree =', self.__Nextfree)
        print('{0:^5}|{1:^20}|{2:^5}'.format('Node', 'Data', 'Pointer'))
        for i in range(len(self.__queue)):
            print('{0:^5}|{1:^20}|{2:^5}'.format(i,
                                                 self.__queue[i].getData(),
                                                 self.__queue[i].getPointer()))
