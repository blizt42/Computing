class Node:
    def __init__(self,data, pointer = -1):
        self.__data = data
        self.__Pointer = pointer

    def getData(self):
        return self.__data
    def getPointer(self):
        return self.__Pointer

    def setData(self, data):
        self.__data = data
    def setPointer(self, pointer):
        self.__Pointer = pointer

class LinkedList:
    def __init__(self, size):
        self.__LL = [Node('Empty', i+1 if i != size-1 else -1) for i in range(size)]
        self.__NFpointer = 0 # THE NEW NODE POINTER
        self.__head = -1

    def display(self):
        print('Start = ', self.__head)
        print('Next free = ',self.__NFpointer)
        print('{:^5}|{:^20}|{:^5}'.format('Node', 'Data','Pointer'))
        for i in range(len(self.__LL)):
            print('{:^5}|{:^20}|{:^5}'.format(i ,
                                              self.__LL[i].getData(),
                                              self.__LL[i].getPointer()))

    def insert(self, data):
        if self.__NFpointer == -1:
            print('No more free space.')
            return
        self.__LL[self.__NFpointer].setData(data)
        if self.__head == -1: # Store into empty list
            temp = self.__LL[self.__NFpointer].getPointer()
            self.__LL[self.__NFpointer].setPointer(-1)
            self.__head = self.__NFpointer
            self.__NFpointer = temp
        else:
            previous = -1
            current = self.__head
            while current != -1:
                if data < self.__LL[current].getData():
                    break
                previous = current
                current = self.__LL[current].getPointer()
            if previous == -1: # Store as first node in the list with items
                temp = self.__LL[self.__NFpointer].getPointer()
                self.__LL[self.__NFpointer].setPointer(self.__head)
                self.__head = self.__NFpointer
                self.__NFpointer = temp
            else: # Store as a node that is not first in the list
                temp = self.__LL[self.__NFpointer].getPointer()
                self.__LL[self.__NFpointer].setPointer(current)
                self.__LL[previous].setPointer(self.__NFpointer)
                self.__NFpointer = temp

    def delete(self, data):
        if self.__head == -1:
            print('List is empty!')
            return
        previous = -1
        current = self.__head
        while current != -1:
            if data == self.__LL[current].getData():
                break
            previous = current
            current = self.__LL[current].getPointer()
        if current == -1:
            print(f'Data {data} is not found!')
            return
        if previous == -1:
            temp = self.__NFpointer
            self.__NFpointer = self.__head
            self.__head = self.__LL[current].getPointer()
            self.__LL[current].setPointer(temp)
        else:
            temp = self.__NFpointer
            self.__NFpointer = current
            self.__LL[previous].setPointer(self.__LL[current].getPointer())
            self.__LL[current].setPointer(temp)

    def search(self, data):
        # NOT NEEDED
        # if self.__head == -1:
        #     print('List is empty!')
        #     return

        current = self.__head
        while current != -1 and self.__LL[current].getData() <= data:
            if data == self.__LL[current].getData():
                print(f'Data {data} found in Node {current}')
                # break
                return
            current = self.__LL[current].getPointer()
        print(f'Data {data} not found')
        # if current == -1:
        #     print(f'Data {data} not found')
        # else:
        #     print(f'Data {data} found in Node {current}')

    def printInOrder(self):
        if self.__head != -1:
            print('List in Alphabetical order:')
            current = self.__head
            while current != -1:
                print(self.__LL[current].getData())
                current = self.__LL[current].getPointer()
        else:
            print('List is empty!')


link = LinkedList(2)
link.display()
link.insert('A')
link.insert('C')
link.insert('B')
link.delete('A')
link.delete('C')
link.display()