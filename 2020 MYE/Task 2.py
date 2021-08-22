class Block:
    def __init__(self, dt = None, phash = None, chash = None, nxt = None):
        self.__data = dt
        self.__prevhash = phash
        self.__currhash = chash
        self.__next = nxt

    def setData(self, dt):
        self.__data = dt
    def getData(self):
        return self.__data

    def setprevHash(self, phash):
        self.__prevhash = phash
    def getprevHash(self):
        return self.__prevhash

    def setcurrHash(self, chash):
        self.__currhash = chash
    def getcurrHash(self):
        return self.__currhash

    def setNext(self, nxt):
        self.__next = nxt
    def getNext(self):
        return self.__next

    def ComputeHash(self, data, phash):
        total = 0
        for char in data:
            total += ord(char)
        den = 0
        denlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        prevhash = phash[::-1]
        for i in range(len(prevhash)):
            phex = denlist.index(prevhash[i])
            den += phex * 16 ** i
        total += den
        nhex = []
        while total >= 16:
            nhex.append(str(total % 16))
            total = total // 16
        nhex.append(str(total))
        currhash = ''
        for i in range(len(nhex)):
            currhash += denlist[int(nhex[len(nhex) - 1 - i])]
        return currhash

class Blockchain:
    def __init__(self):
            self.__blockchain = [Block('None', 'None', 'None', i+1) for i in range(20)]
            self.__start = -1
            self.__nextfree = 0

    def display(self):
        print('Block |          Data          | prevhash | currHash | Next')
        for i in range(len(self.__blockchain)):
            print('{:^5} | {:^22} | {:^8} | {:^8} | {:^4}'.format(i,
                                                                 self.__blockchain[i].getData(),
                                                                 self.__blockchain[i].getprevHash(),
                                                                 self.__blockchain[i].getcurrHash(),
                                                                 self.__blockchain[i].getNext()))
        #print('nextfree: ', self.__nextfree)
        #print('start: ', self.__start)

    def insert(self, data):
        self.__blockchain[self.__nextfree].setData(data)
        if self.__start == -1:
            temp = self.__blockchain[self.__nextfree].getNext()
            self.__blockchain[self.__nextfree].setprevHash('983')
            self.__blockchain[self.__nextfree].setcurrHash(
                self.__blockchain[self.__nextfree].ComputeHash(self.__blockchain[self.__nextfree].getData(),
                                                               self.__blockchain[self.__nextfree].getprevHash())
            )
            self.__blockchain[self.__nextfree].setNext(-1)
            self.__start = self.__nextfree
            self.__nextfree = temp
            return
        else:
            current = self.__start
            while self.__blockchain[current].getNext() != -1:
                current = self.__blockchain[current].getNext()
            self.__blockchain[current].setNext(self.__nextfree)
            self.__blockchain[self.__nextfree].setprevHash(self.__blockchain[current].getcurrHash())

        temp = self.__blockchain[self.__nextfree].getNext()
        self.__blockchain[self.__nextfree].setcurrHash(
        self.__blockchain[self.__nextfree].ComputeHash(self.__blockchain[self.__nextfree].getData(),
                                                       self.__blockchain[self.__nextfree].getprevHash())
        )
        self.__blockchain[self.__nextfree].setNext(-1)
        self.__nextfree = temp



def ComputeHash(data, phash):
    total = 0
    for char in data:
        total += ord(char)
    den = 0
    denlist = ['0', '1','2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prevhash = phash[::-1]
    for i in range(len(prevhash)):
        phex = denlist.index(prevhash[i])
        den += phex * 16**i
    total += den
    nhex = []
    while total >= 16:
        nhex.append(str(total % 16))
        total = total // 16
    nhex.append(str(total))
    currhash = ''
    for i in range(len(nhex)):
        currhash += denlist[int(nhex[len(nhex)-1-i])]
    return currhash

#print(ComputeHash('123-23345-3:1507000.85','983'))


bc = Blockchain()
#bc.insert('123-23345-3:1507000.85')
file = open('BANKRECORDS.txt', 'r')
for line in file:
    record = line.strip()
    print(record)
    bc.insert(record)
bc.display()
