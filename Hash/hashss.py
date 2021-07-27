#assume 0 based index
#pg 4 hash table
##print(hashF("A5RD", 9))
##print(hashF("B7MF", 9))
##print(hashF("R2YJ", 9))
##print(hashF("J6TR", 9))
size = 9
def hashF(key, size):
    total = 0
    for char in key:
        total += ord(char) #returns ascii value of char
    return total % size

def CreateHashTable():
    hashtable = [['',''] for i in range(size)]
    return hashtable

def AddRecord(filename):
    readFile = open(filename, 'r')
    lines = readFile.readlines()
    for line in lines:
        line = line.strip()
        CustomerID, Name = line.split(',')
        index = hashF(CustomerID, size)
        print('debug', index)
        print(hashT[index][0])
        while hashT[index][0] != '':
            index = (index+1) % size
        hashT[index] = [CustomerID, Name]
        print(hashT[index], "added to Hash table at item: ", index)


hashT = CreateHashTable()
AddRecord('customers.txt')
