class record:
    def __init__(self, name, num):
        self.__PersonName = name
        self.__TelephoneNo= num

    def getPersonName(self):
        return self.__PersonName
    def setPersonName(self, name):
        self.__PersonName = name

    def getTelephoneNo(self):
        return self.__TelephoneNo
    def setTelephoneNo(self, num):
        self.__TelephoneNo = num

class recordlist:
    def __init__(self, size = 500):
        self.__list = [record('','') for i in range(size)]

    def insert(self, index, name, num):
        self.__list[index].setPersonName(name)
        self.__list[index].setTelephoneNo(num)

    def Search(self, SearchName):
        HashTotal = 0
        position = 1
        for char in SearchName:
            ascii = ord(char)
            HashTotal += ascii * position
            position+=1
        hashValue = HashTotal % 500
        print(f'{tosearch}"s value is {hashValue}')
        return hashValue

    def Search2(self, SearchName):
        HashTotal = 0
        position = 1
        for char in SearchName:
            ascii = ord(char)
            HashTotal += ascii * position
            position += 1
        hashValue = HashTotal % 500
        while self.__list[hashValue].getPersonName() != tosearch:
            print(self.__list[hashValue].getPersonName(), tosearch)
            if self.__list[hashValue].getPersonName() == '':
                print(f'{tosearch} is NOT FOUND')
                return
            hashValue+= 1
        print(f'{tosearch}"s value is {hashValue}')
        return hashValue

    def DisplayValues(self):
        print('{:^5}|{:^15}|{:^15}'.format('Index', 'Name', 'Telephone No.'))
        for i in range(len(self.__list)):
            print('{:^5}|{:^30}|{:^15}'.format(i,
                                               self.__list[i].getPersonName(),
                                               self.__list[i].getTelephoneNo()))



if __name__ == '__main__':
    recordlist = recordlist()
    file = open('HASHEDDATA.txt', 'r')
    for line in file:
        line = line.strip().split(',')
        if line[1] != '':
            recordlist.insert(int(line[0]), line[1], line[2])
    file.close()
    # recordlist.DisplayValues()
    tosearch = input('Enter name to search: ')
    hashV = recordlist.Search(tosearch)
    hashV2 = recordlist.Search2(tosearch)

