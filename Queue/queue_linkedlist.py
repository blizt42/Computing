#code not by me
class Node():
    def __init__(self,data): #constructor
        self.__data = data
        self.__ptr  = None

    def getData(self):
        return self.__data

    def getPtr(self):
        return self.__ptr

    def setData(self, data):
        self.__data = data

    def setPtr(self, ptr):
        self.__ptr = ptr

class QueueLL():
    def __init__(self): #constructor
        self.__front = None #front pointer of queue
        self.__limit = int(input("Enter size of queue:\n>>> ")) #max size of queue
        self.__size  = 0 #current size of queue
#        self.__rear  = None #rear pointer of queue (Not implemented here)

    def display(self): #display queue
        temp = self.__front
        while temp!= None:
            print(temp.getData())
            temp = temp.getPtr()
            
    def __str__(self): #display queue using print built-in function
        text=''
        temp = self.__front
        while temp != None:
            text = text + temp.getData() + '|'
            temp = temp.getPtr()
        text = text[:-1] #get rid of last char '|'
        return text+'\n'
            
    def insert(self, data):
        if self.__size == self.__limit: #check for overflow
            print( "Queue Overflow") #error message
            return
        else:
            newnode = Node(data) #grab node from memory (no free space list)
            if self.__front == None:
                self.__front = newnode
                self.__size += 1
            else: #traverse to the end of linked list(queue)
                temp = self.__front
                rear = None
                while temp != None:
                    rear = temp
                    temp = temp.getPtr()
                rear.setPtr(newnode)
                self.__size += 1
        
    def delete(self):
        if self.__size == 0: #check for underflow
            print("Queue Underflow") #error message
            return
        else: #remove first node from linked list(queue)
            temp = self.__front
            self.__front = temp.getPtr()
            self.__size -= 1

inp = -1
while inp != 5:
    print("1. Initialise Queue")
    print("2. Insert in Queue")
    print("3. Delete from Queue")
    print("4. Display Queue")
    print("5. Exit")
    inp = int(input("Enter your choice:\n>>> "))
    if inp == 1:
        q1 = QueueLL()
    if inp == 2:
        q1.insert(input("Enter value to insert:\n>>> "))
    if inp == 3:
        q1.delete()
    if inp == 4:
##        q1.display() #using display method
        print(q1) #using __str__ methiod






