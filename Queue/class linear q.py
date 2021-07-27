class queue:
    def __init__(self, size =5):
        self.__list = ['' for i in range(size)]
        self.__front = -1
        self.__rear = 0
        self.__size = size

    def getList(self):
        return self.__list
    def getFront(self):
        return self.__front
    def getRear(self):
        return self.__rear

    def isEmpty(self):
        return self.__front == -1 and self.__rear == 0
    def isFull(self):
        return self.__front == 0 and self.__rear == self.__size -1
    def isEnd(self):
        return self.__rear == self.__size -1

    def enqueue(self, item):
        if self.isEnd() is True:
            print('queue is full or has item that occupies last slot, please dequeue all item first')
            return
##        if self.isFull() is True:
##            print('Full')
##            return
##        elif self.__rear == self.__size -1:
##            print('list has item that occupies last slot, please dequeue all item first')
##            return
        if self.isEmpty() == True:
            self.__front = 0
            self.__list[self.__rear] = item
            print(item, 'added')
            return
        else:
            self.__rear += 1
            self.__list[self.__rear] = item
            print(item,'added')
            return

    def dequeue(self):
        if self.isEmpty() == True:
            print('empty')
            return
        if self.__front == self.__rear:
            self.__list = ['' for i in range(self.__size)]
            self.__front = -1
            self.__rear = 0
            print('queue has been reset')
        else:
            self.__list[self.__front] = ''
            self.__front += 1

    def display(self):
        count = 0
        for item in self.__list:
            count += 1
            print(f'item {count}:',item)
        
#main program
def fulltest():
    q = queue(5)
    for i in range(6):
        q.enqueue(f'number {i+1}')
    q.display()
    print(q.getFront())
    print(q.getRear())
    for i in range(6):
        q.dequeue()
    q.display()
    print()
    
    l =  queue(4)
    for i in range(4):
        l.enqueue(f'letter{i+1}')
    l.dequeue()
    l.display()
    l.enqueue('last')
    l.display()
    print()

    a = queue(5)
    for i in range(3):
        a.enqueue(f'symbol {i+1}')
    a.display()
    for i in range(4):
        a.dequeue()
    a.display()
    
    
fulltest()   




