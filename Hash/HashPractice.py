class Hash:
    def __init__(self, size):
        self.__size = size
        self.__Table = [['',''] for i in range(size)]

    def HashFunction(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.__size

    def AddRecord(self, record):
        index = self.HashFunction(record)
        while self.__Table[index][0] != '':
            print(self.__Table[index])
            index = (index+1) % self.__size
        self.__Table[index] = [index, record]
        print(self.__Table[index][1], 'added to hash table at: ', index)

table = Hash(9)
table.AddRecord("A5RD")
table.AddRecord("B7MF")
table.AddRecord("R2YJ")
table.AddRecord("J6TR")