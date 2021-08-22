class Node:
    def __init__(self, leftP, data, rightP):
        self.__leftP = leftP
        self.__data = data
        self.__rightP = rightP

    def getleftP(self):
        return self.__leftP
    def getdata(self):
        return self.__data
    def getrightP(self):
        return self.__rightP

    def setleftP(self, leftP):
        self.__leftP = leftP
    def setrightP(self, rightP):
        self.__rightP = rightP
    def setdata(self, data):
        self.__data = data

# main program
class BinaryTree:
    def __init__(self):
        self.__root = -1
        self.__nextfreePos = 0

        # create array of size 20 each with a Node of (leftP, data, rightP)
        self.__thisTree = [Node(i + 1 if i != 19 else -1,'',-1) for i in range(20)]

    def getroot(self):
        return self.__root
    def getnextfreePos(self):
        return self.__nextfreePos

    def setroot(self, root):
        self.__root = root
    def setnextfreePos(self, nfPos):
        self.__nextfreePos = nfPos

    def additemtobinaryTree(self, newfreeItem):
        if self.getroot() == -1:
            self.setroot(self.getnextfreePos())
            self.setnextfreePos(self.__thisTree[self.getnextfreePos()].getleftP())
            # self.__nextfreePos = self.__thisTree[self.__nextfreePos].getleftP()
            self.__thisTree[self.__root].setdata(newfreeItem)
            self.__thisTree[self.__root].setleftP(-1)
        else:
            # traverse the tree to find the pos for the newfreeItem
            currentPos = self.getroot()
            lastMove = 'X'
            while True:
                previousPos = currentPos
                if newfreeItem < self.__thisTree[currentPos].getdata():
                    # move to left
                    lastMove = 'L'
                    currentPos = self.__thisTree[currentPos].getleftP()
                else:
                    # move to right
                    lastMove = 'R'
                    currentPos = self.__thisTree[currentPos].getrightP()
                print(lastMove)
                print(currentPos, previousPos)
                if currentPos == -1: # terminating condition
                    break
            if lastMove == 'R':
                self.__thisTree[previousPos].setrightP(self.__nextfreePos)
            else: # Last Move is 'L'
                self.__thisTree[previousPos].setleftP(self.__nextfreePos)

            # add new node
            self.__thisTree[self.__nextfreePos].setdata(newfreeItem)
            self.__thisTree[self.__nextfreePos].setleftP(-1)
            self.__nextfreePos = self.__thisTree[self.__nextfreePos].getleftP()

bt = BinaryTree()
bt.additemtobinaryTree('Clement')
bt.additemtobinaryTree('Dylan')
bt.additemtobinaryTree('Ahennian')