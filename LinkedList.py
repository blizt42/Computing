class Node:
    def __init__(self, name, pointer = -1):
        self.name = name
        self.pointer = pointer
    def getName(self):
        return self.name
    def getPointer(self):
        return self.pointer
    def setPointer(self, pointer):
        self.pointer = pointer
    def setName(self, name):
        self.name = name

class linkedlist:
    def __init__(self, size):
        self.Make = [Node("") for i in range(size)]
        for i in range(len(self.Make)-1):
            self.Make[i].setPointer(1+i)
        self.nextfree = 0
        self.start = -1
    def display(self):
        print("start=",self.start)
        print("nextfree=",self.nextfree)
        print("{0:^4}|{1:^20}|{2:^4}".format("Index","Car","Pointer"))
        for i in range(len(self.Make)):
           print("{0:^4}|{1:^20}|{2:^4}".format(i, self.Make[i].getName(),
                        self.Make[i].getPointer()))
                
    def insert(self, newData):
        if self.nextfree == -1:
            print("No free node avaiable")
            return False
        self.Make[self.nextfree].setName(newData)
        if self.start == -1:
            temp = self.Make[self.nextfree].getPointer()
            self.start = self.nextfree
            self.Make[self.nextfree].setPointer(-1)
            self.nextfree = temp
        else:
            current = self.start
            previous =- 1
            while current !=-1:
                if self.Make[current].getName() >  newData:
                    break
                previous = current
                current = self.Make[current].getPointer()
            
            if previous == -1:
                temp = self.Make[self.nextfree].getPointer()
                self.start = self.nextfree
                self.Make[self.nextfree].setPointer(current)
                self.nextfree = temp
            else:
                temp = self.Make[self.nextfree].getPointer()
                self.Make[previous].setPointer(self.nextfree)
                self.Make[self.nextfree].setPointer(current)
                self.nextfree = temp

    def delete(self, data):
        if self.nextfree == -1:
            print("No free node available")
            return False
        previous = -1
        current = self.start
        while current != -1:
            if data == self.Make[current].getName():
                self.Make[current].setName("empty")
                break
            previous = current
            current = self.Make[current].getPointer()
            
        if current == -1:
            print("The node is not found in the list")
            return False
        if previous == -1:
            temp = self.nextfree
            self.nextfree = self.start
            self.start = self.Make[current].getPointer()
            self.Make[current].setPointer(temp)
        else:
            temp = self.nextfree
            self.nextfree = current
            self.Make[previous].setPointer(self.Make[current].getPointer())
            self.Make[current].setPointer(temp)
            
    def search(self, data):
        current = self.start
        while current != -1 and self.Make[current].getName() <= data:
            if data == self.Make[current].getName():
                print("{} found at index {}".format(data, current))
                return
            current = self.Make[current].getPointer()
        print("{} not found in list".format(data))
LL = linkedlist(5)
LL.insert('b')
LL.insert('a')
LL.insert('d')
LL.insert('c')
LL.display()
LL.delete('b')
LL.display()
LL.search('b')
LL.search('a')
            
