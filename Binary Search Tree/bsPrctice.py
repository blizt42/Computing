NullPointer = -1

class TreeNode:
    def __init__(self, data = '', lp = None, rp = None):
        self.__Data = data
        self.__leftPointer = lp
        self.__rightPointer = rp

    def getData(self):
        return self.__Data
    def setData(self, data):
        self.__Data = data

    def getLeftPtr(self):
        return self.__leftPointer
    def setLeftPtr(self, lp):
        self.__leftPointer = lp

    def getRightPtr(self):
        return self.__rightPointer
    def setRightPtr(self, rp):
        self.__rightPointer = rp

class BST:
    def __init__(self, size = 5):
        self.__Tree = [TreeNode('', i+1, -1) for i in range(size)]
        self.__RootPtr = NullPointer
        self.__FreePtr = 0
        self.__Tree[size-1].setLeftPtr(NullPointer)

    def getRootPtr(self):
        return self.__RootPtr

    def display(self):
        print(self.__Tree[self.__FreePtr].getLeftPtr(), self.__FreePtr)
        print('RootPtr: ', self.__RootPtr)
        print('FreePtr: ', self.__FreePtr)
        for i in range(len(self.__Tree)):
            print('{:^5}|{:^8}|{:^5}'.format(self.__Tree[i].getLeftPtr(),
                                             self.__Tree[i].getData(),
                                             self.__Tree[i].getRightPtr()))

    def InsertNode(self, item):
        if self.__FreePtr == NullPointer:
            print('No free available Node')
            return

        #print(self.__Tree[self.__FreePtr].getLeftPtr(), self.__FreePtr)
        NewNodePtr = self.__FreePtr
        self.__FreePtr = self.__Tree[self.__FreePtr].getLeftPtr()
        self.__Tree[NewNodePtr].setData(item)
        self.__Tree[NewNodePtr].setLeftPtr(NullPointer)
        self.__Tree[NewNodePtr].setRightPtr(NullPointer)
        #print(self.__Tree[self.__FreePtr].getLeftPtr(), self.__FreePtr)

        if self.__RootPtr == NullPointer:
            self.__RootPtr = NewNodePtr
        else:
            current = self.__RootPtr
            while current != NullPointer:
                previous = current
                if self.__Tree[current].getData() > item:
                    TurnLeft = True
                    current = self.__Tree[current].getLeftPtr()
                else:
                    current = self.__Tree[current].getRightPtr()
                    TurnLeft = False
            if TurnLeft == True:
                self.__Tree[previous].setLeftPtr(NewNodePtr)
            else:
                self.__Tree[previous].setRightPtr(NewNodePtr)

    def Inorder(self, index):
        if index != NullPointer:
            self.Inorder(self.__Tree[index].getLeftPtr())
            print(self.__Tree[index].getData())
            self.Inorder(self.__Tree[index].getRightPtr())

    def Preorder(self, index):
        if index != NullPointer:
            print(self.__Tree[index].getData())
            self.Preorder(self.__Tree[index].getLeftPtr())
            self.Preorder(self.__Tree[index].getRightPtr())

    def Postorder(self, index):
        if index != NullPointer:
            self.Postorder(self.__Tree[index].getLeftPtr())
            self.Postorder(self.__Tree[index].getRightPtr())
            print(self.__Tree[index].getData())

    def Find(self, item):
        current = self.__RootPtr
        while current != NullPointer and self.__Tree[current].getData() != item:
            if item < self.__Tree[current].getData():
                current = self.__Tree[current].getLeftPtr()
            else:
                current = self.__Tree[current].getRightPtr()


        return 'Not Found' if current == NullPointer else current


def main():
    tree = BST(7)
    tree.InsertNode('Mango')
    tree.InsertNode('Durian')
    tree.InsertNode('Papaya')
    tree.InsertNode('Apple')
    tree.InsertNode('Banana')
    tree.InsertNode('Zhennian')
    tree.InsertNode('Apple')
    tree.display()
    tree.Preorder(tree.getRootPtr())
    print(tree.Find('eian'))

main()

# tree = BST(20)
# tree.display()
# tree.InsertNode('Mango')
# tree.display()