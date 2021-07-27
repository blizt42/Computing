class circular:
    def __init__(self, limit =5):
        self.__list = ['' for i in range(limit)]
        self.__front = 1
        self.__rear = limit
        self.__limit = limit
        self.__size = 0

    def getList(self):
        return self.__list
    def getFront(self):
        return self.__front
    def getRear(self):
        return self.__rear

    def isEmpty(self):
        return self.__size == 0
    def isFull(self):
        return self.__size == self.__limit

    def enqueue(self, item):
        if self.isFull() is True:
            print('Queue overflow')
            return
        else:
            if self.__rear == self.__limit:
                self.__rear = 1
            else:
                self.__rear += 1
            self.__list[self.__rear-1]= item
            self.__size += 1
        return

    def dequeue(self):
        if self.isEmpty() is True:
            return print('Queue Underflow')
        else:
            self.__list[self.__front-1] = ''
            self.__size = self.__size -1
            if self.__front == self.__limit:
                self.__front = 1
                return
            else:
                self.__front += 1
            

    def display(self):
        count = 0
        for item in self.__list:
            count += 1
            print(f'item {count}', item)
        #print()

    def pointer(self):
        print('rear',self.__rear)
        print('front', self.__front)
        print()

def main():
    q = circular()
    q.display()
    q.pointer()
    q.enqueue('1')
    q.enqueue('1')
    q.display()
    q.pointer()
    q.enqueue('2')
    q.enqueue('2')
    q.display()
    q.pointer()

    q.dequeue()
    q.dequeue()

    q.enqueue('3')
    q.enqueue('3')
    q.display()
    q.pointer()

    q.dequeue()
    q.dequeue()

    q.enqueue('4')
    q.enqueue('4')
    q.display()
    q.pointer()

main()
            
        

 
            
        
