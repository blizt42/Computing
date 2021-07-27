class Node:
    def __init__(self, data, ptr):
        self.__Data = data
        self.__Ptr = ptr
    def getData(self):
        return self.__Data
    def setData(self, data):
        self.__Data = data

    def getPtr(self):
        return self.__Ptr
    def setPtr(self, ptr):
        self.__Ptr = ptr

class LinkedList:
    def __init__(self, size):
        self.__Start = -1
        self.__NextFree = 0
        self.__LL = [Node('', i+1 if i+1 != size else -1) for i in range(size)]

    def Display(self):
        print('Start: ', self.__Start)
        print('NextFree: ', self.__NextFree)
        print('|{:^5}|{:^8}|{:^13}|'.format('Node', 'Data', 'Pointer'))
        for i in range(len(self.__LL)):
            print('|{:^5}|{:^8}|{:^13}|'.format(i,
                                               self.__LL[i].getData(),
                                               self.__LL[i].getPtr()))

    def Insert(self, data):
        if self.__NextFree == -1:
            print('List is full')
        self.__LL[self.__NextFree].setData(data)
        if self.__Start == -1:
            temp = self.__LL[self.__NextFree].getPtr()
            self.__Start = self.__NextFree
            self.__LL[self.__NextFree].setPtr(-1)
            self.__NextFree = temp
        else:
            current = self.__Start
            previous = -1
            while current != -1:
                if data < self.__LL[current].getData():
                    break
                previous = current
                current = self.__LL[current].getPtr()
            if previous == -1:
                temp = self.__LL[self.__NextFree].getPtr()
                self.__LL[self.__NextFree].setPtr(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = temp
            else:
                temp = self.__LL[self.__NextFree].getPtr()
                self.__LL[self.__NextFree].setPtr(current)
                self.__LL[previous].setPtr(self.__NextFree)
                self.__NextFree = temp

    def Delete(self, data):
        if self.__Start == -1:
            print('List is empty!')
            return
        previous = -1
        current = self.__Start
        while current != -1:
            if self.__LL[current].getData() == data:
                break
            previous = current
            current = self.__LL[current].getPtr()
        if current == -1:
            print('Data Not found')
            return
        if previous == -1:
            temp = self.__NextFree
            self.__NextFree = self.__Start
            self.__Start = self.__LL[current].getPtr()
            self.__LL[current].setPtr(temp)
        else:
            temp = self.__NextFree
            self.__NextFree = self.__LL[previous].getPtr()
            self.__LL[previous].setPtr(self.__LL[current].getPtr())
            self.__LL[current].setPtr(temp)

l = LinkedList(4)
l.Display()
l.Insert('A')
l.Insert('C')
l.Insert('B')
l.Insert('D')
#l.Insert('F')
l.Display()
l.Delete('A')
l.Delete('C')
l.Delete('B')
l.Delete('F')
l.Delete('D')
l.Delete('e')
l.Display()
