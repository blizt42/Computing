NullPointer = 0

class TreeNode:
    def __init__(self,data = '', left = 0, right = 0):
        self.__Data = data
        self.__LeftPointer = left
        self.__RightPointer = right

    def getData(self):
        return self.__Data
    def getLeftPointer(self):
        return self.__LeftPointer
    def getRightPointer(self):
        return self.__RightPointer

    def setData(self, data):
        self.__Data = data
    def setLeft(self, left):
        self.__LeftPointer = left
    def setRight(self, right):
        self.__RightPointer = right

class BST:
    def __init__(self, size = 7):
        self.__Tree  = ['MyTree']+[TreeNode() for i in range(size)]
        self.__RootPointer = NullPointer
        self.__FreePtr = 1
        for i in range(1, size):
            self.__Tree[i].setLeft(i+1)
        self.__Tree[size].setLeft(NullPointer)

    def display(self):
        print('RootPointer =', self.__RootPointer)
        print('Free Pointer =', self.__FreePtr)
        for i in range(1,len(self.__Tree)):
            print('{:^5}|{:^8}|{:^13}'.format(self.__Tree[i].getLeftPointer(),\
                  self.__Tree[i].getData(),\
                  self.__Tree[i].getRightPointer()))

    def InsertNode(self, Newitem):
        if self.__FreePtr != NullPointer:
            NewNodePtr = self.__FreePtr
            self.__FreePtr = self.__Tree[self.__FreePtr].getLeftPointer()
            self.__Tree[NewNodePtr].setData(Newitem)
            self.__Tree[NewNodePtr].setLeft(NullPointer)
            self.__Tree[NewNodePtr].setRight(NullPointer)

            if self.__RootPointer == NullPointer:
                self.__RootPointer = NewNodePtr
            else:
                cur = self.__RootPointer
                while cur != NullPointer:
                    prev = cur
                    if Newitem < self.__Tree[cur].getData():
                        TurnedLeft = True
                        cur = self.__Tree[cur].getLeftPointer()
                    else:
                        TurnedLeft = False
                        cur = self.__Tree[cur].getRightPointer()
                if TurnedLeft == True:
                    self.__Tree[prev].setLeft(NewNodePtr)
                else:
                    self.__Tree[prev].setRight(NewNodePtr)
        return 'no free node avail'

    def Inorder(self, index):
        if index != NullPointer:
            self.Inorder(self.__Tree[index].getLeftPointer())
            print(self.__Tree[index].getData())
            self.Inorder(self.__Tree[index].getRightPointer())

    def Preorder(self, index):
        if index != NullPointer:
            print(self.__Tree[index].getData())
            self.Inorder(self.__Tree[index].getLeftPointer())
            self.Inorder(self.__Tree[index].getRightPointer())

    def Postorder(self, index):
        if index != NullPointer:
            self.Inorder(self.__Tree[index].getLeftPointer())
            self.Inorder(self.__Tree[index].getRightPointer())
            print(self.__Tree[index].getData())

    def getRootPtr(self):
        return self.__RootPointer
    def getTree(self):
        return self.__Tree

    def Search(self, searchitem):
        cur = self.__RootPointer
        while cur  != NullPointer and self.__Tree[cur].getData() != searchitem:
            if searchitem < self.__Tree[cur].getData():
                cur = self.__Tree[cur].getLeftPointer()
            else:
                cur = self.__Tree[cur].getRightPointer()

        return cur
        

def main():
    tree = BST()
    tree.InsertNode('Mango')
    tree.InsertNode('Durian')
    tree.InsertNode('Papaya')
    tree.InsertNode('Apple')
    tree.InsertNode('Banana')
    tree.InsertNode('Zhennian')
    
    tree.InsertNode('Apple')
    tree.display()
    tree.Inorder(tree.getRootPtr())
    print(tree.Search('Zhennian'))
main()
