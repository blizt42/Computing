#Implement a queue data structure storing names of customers.
#Data is stored into a zero-based array of up to the size specified.

#Variables front, rear and size are initialised in the main program where
#front and rear point to the first and last names in the queue respectively.

#Code using OOP.

class Queue:
       def __init__(self,size): #constructor
              self.maxSize = size #maxSize is the total capacity of queue
              self.data = [""]*self.maxSize
              self.front = -1
              self.rear = -1

       def IsEmpty(self):
              return (self.front == -1 and self.rear == -1)

       def IsFull(self):
              if (self.rear == self.front - 1) or (self.front == 0 and self.rear == self.maxSize - 1):
                     return True
              return False
              #Alternatively, use (self.Rear + 1) % len(self.Items) == self.Front

       def NumberItems(self):
              if self.IsEmpty():
                     return 0
              if self.IsFull():
                     return self.maxSize
              if self.rear >= self.front:
                     return self.rear - self.front + 1
              if self.rear < self.front:
                     return self.maxSize - self.front + self.rear + 1
              
       def getFront(self):
              return self.front

       def getRear(self):
              return self.rear

       def Enqueue(self, item): #increment rear then add
              if self.IsFull():  #queue is full
                     print("Circular queue is full. Enqueue not performed!")
                     return
              else:
                     #item = input("Enter name of next customer: ")
                     if self.IsEmpty(): #queue is empty
                            self.front = 0
                            self.rear = 0
                            self.data[self.rear] = item
                            print("New first customer added!")
                            return
                     else:
                            self.rear = (self.rear + 1) % self.maxSize
                            self.data[self.rear] = item
                            print("New customer added!")                     
                     return
              
       def Dequeue(self):
              if self.IsEmpty(): #queue is empty
                     print("Circular queue is empty. Dequeue not performed!")
                     return
              else:
                     if self.NumberItems() == 1:#last name dequeuED, i.e.: queue becomes empty
                            print(self.data[self.front], "has been dequeued.")
                            self.front = -1    #reinitialises front
                            self.rear = -1     #reinitialises rear
                            return
                     else:
                            print(self.data[self.front], "has been dequeued.")
                            self.front = (self.front + 1) % self.maxSize #pointer moves to next name in queue
                            return
              return
              
       def Display(self):
              i = 0
              if self.IsEmpty():
                     print("Queue is empty")
                     return
              else:
                     print("----------------------------------")
                     print("Front pointer: ", str(self.getFront()))
                     print("Rear pointer: ", str(self.getRear()))
                     i = self.getFront()
                     print("|{0:^8}|{1:^15}|{2:^10}|".format("Item", "Name", "Pointer"))
                     print("----------------------------------")
                     while i != self.getRear():
                          if i == self.getFront():
                                 print("|{0:^8}|{1:^15}|{2:^10}|".format(i, self.data[i], "Front"))                                 
                          else:
                                 print("|{0:^8}|{1:^15}|{2:^10}|".format(i, self.data[i], "-"))
                          i = (i+1) % self.maxSize
                     if i == self.getFront() and i == self.getRear():
                            print("|{0:^8}|{1:^15}|{2:^10}|".format(i, self.data[i], "Front|Rear"))
                     else:
                            print("|{0:^8}|{1:^15}|{2:^10}|".format(i, self.data[i], "Rear"))#NOT NICELY WRITTEN
                     print("----------------------------------")
                     return
       def Display2(self):
              i = 0
              if self.IsEmpty():
                     print("Queue is empty")
                     return
              else:
                     print("----------------------------------")
                     print("Front pointer: ", str(self.getFront()))
                     print("Rear pointer: ", str(self.getRear()))
                     
                     print("|{0:^8}|{1:^15}|{2:^7}|".format("Item", "Name", "Pointer"))
                     print("----------------------------------")
                     for item in self.data:
                            if i == self.getFront():
                                   print("|{0:^8}|{1:^15}|{2:^7}|".format(i, item, "FRONT"))
                            elif i == self.getRear():
                                   print("|{0:^8}|{1:^15}|{2:^7}|".format(i, item, "REAR"))
                            else:
                                   print("|{0:^8}|{1:^15}|{2:^7}|".format(i, item, "--"))
                            i = i + 1
                     print("------------------------------")
                     return
#main program
##q1 = Queue(4)
##print(q1.IsEmpty())
##print(q1.IsFull())
##print(q1.NumberItems())
##q1.Enqueue("Ali")
##q1.Enqueue("Bala")
##q1.Enqueue("Clement")
##q1.Enqueue("Don")
##q1.Enqueue("Eric")
##q1.Display()
##print(q1.NumberItems())
##q1.Dequeue()
##q1.Dequeue()
##q1.Dequeue()
##q1.Dequeue()
##q1.Dequeue()
##q1.Display()
##print(q1.NumberItems())
##q1.Enqueue("Alice")
##q1.Enqueue("Betty")
##q1.Enqueue("Cindy")
##q1.Enqueue("Dana")
##q1.Dequeue()
##q1.Dequeue()
##q1.Enqueue("Elle")
##q1.Enqueue("Fiona")
##q1.Enqueue("Goh Xiaomei")
##q1.Display()
##print(q1.NumberItems())
