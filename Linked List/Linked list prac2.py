class Node:
    def __init__(self, data, pointer):
        self.__data = data
        self.__pointer = pointer

    def getData(self):
        return self.__data
    def getPointer(self):
        return self.__pointer

    def setData(self, data):
        self.__data = data
    def setPointer(self, pointer):
        self.__pointer = pointer

class LinkedList:
    def __init__(self, size):
        self.__LL = [Node('Empty', i + 1 if i < size-1 else -1) for i in range(size)]
        self.__nextfree = 0
        self.__start = -1

    def display(self):
        print('Start = ', self.__start)
        print('Next free = ', self.__nextfree)
        print('{:^5}|{:^20}|{:^5}'.format('Node', 'Data', 'Pointer'))
        for i in range(len(self.__LL)):
            print('{:^5}|{:^20}|{:^5}'.format(i,
                                              self.__LL[i].getData(),
                                              self.__LL[i].getPointer()))

    def insert(self, data):
        if self.__nextfree == -1:
            print('List is full!')
            return
        self.__LL[self.__nextfree].setData(data)
        if self.__start == -1:
            temp = self.__LL[self.__nextfree].getPointer()
            self.__start = self.__nextfree
            self.__LL[self.__nextfree].setPointer(-1)
            self.__nextfree = temp
        else:
            previous = -1
            current = self.__start
            while current != -1:
                if data < self.__LL[current].getData():
                    break
                previous = current
                current = self.__LL[current].getPointer()
            if previous == -1:
                temp = self.__LL[self.__nextfree].getPointer()
                self.__LL[self.__nextfree].setPointer(self.__start)
                self.__start = self.__nextfree
                self.__nextfree = temp
            else:
                temp = self.__LL[self.__nextfree].getPointer()
                self.__LL[self.__nextfree].setPointer(current)
                self.__LL[previous].setPointer(self.__nextfree)
                self.__nextfree = temp

    def delete(self, data):
        if self.__start == -1:
            print('List is empty!')
            return
        previous = -1
        current = self.__start
        while current != -1:
            if data == self.__LL[current].getData():
                break
            previous = current
            current = self.__LL[current].getPointer()
        if previous == -1:
            temp = self.__nextfree
            self.__nexfree = self.__start
            self.__start = self.__LL[current].getPointer()
            self.__LL[current].setPointer(temp)
        else:
            temp = self.__nextfree
            self.__nextfree = current
            self.__LL[previous].setPointer(self.__LL[current].getPointer())
            self.__LL[current].setPointer(temp)

ll = LinkedList(4)
ll.insert('A')
ll.insert('C')
ll.insert('B')
ll.insert('Y')
ll.insert('X')
ll.delete('A')
ll.display()