class ConnectionNode:
    def __init__(self, d, l, r):
        self.__DataValue = d
        self.__LeftChild =  l
        self.__RightChild = r

    def get_DataValue(self):
        return self.__DataValue
    def get_LeftChild(self):
        return self.__LeftChild
    def get_RightChild(self):
        return self.__RightChild

    def set_DataValue(self, d):
        self.__DataValue = d
    def set_LeftChild(self, l):
        self.__LeftChild = l
    def set_RightChild(self, r):
        self.__RightChild = r

class RobotTree:
    def __init__(self, size = 25):
        self.__RobotData = [ConnectionNode('', i+1 if i != size-1 else -1, -1) for i in range(size)]
        self.__Root = 0
        self.__NextFreeChild = 0

    def FindNode(self, NodeValue):
        Found = False
        CurrentPosition = self.__Root
        while Found == False and CurrentPosition <= 24:
            # print(CurrentPosition)
            if self.__RobotData[CurrentPosition].get_DataValue() == NodeValue:
                Found = True
            else:
                CurrentPosition += 1
        if CurrentPosition > 24:
            return -1
        else:
            return CurrentPosition

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        if self.__Root == 0 and self.__NextFreeChild == 0:
            self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].get_LeftChild()
            self.__RobotData[self.__Root].set_LeftChild(-1)
            self.__RobotData[self.__Root].set_DataValue(NewDataItem)
        else:
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > -1:
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > -1:
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self.__NextFreeChild
                    self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].get_LeftChild()
                    self.__RobotData[ChildPointer].set_LeftChild(-1)
                    self.__RobotData[ChildPointer].set_DataValue(NewDataItem)
                # print(ParentPosition)
                if ThisMove == 'L':
                    self.__RobotData[ParentPosition].set_LeftChild(ChildPointer)
                else:
                    self.__RobotData[ParentPosition].set_RightChild(ChildPointer)

    def OutputData(self):
        print('Root = ',self.__Root+1)
        print('NextFreeChild', self.__NextFreeChild+1)
        print('{:^6}|{:^11}|{:^11}|{:^12}'.format('Node', 'DataValue', 'LeftChild', 'RightChild'))
        for i in range(len(self.__RobotData)):
            print('{:^6}|{:^11}|{:^11}|{:^12}'.format(i + 1,
                                                      self.__RobotData[i].get_DataValue(),
                                                      self.__RobotData[i].get_LeftChild() +1,
                                                      self.__RobotData[i].get_RightChild() +1))

    def preOrderTraversal(self, currentPosition):
        if currentPosition != -1:
            print(self.__RobotData[currentPosition].get_DataValue())
            self.preOrderTraversal(self.__RobotData[currentPosition].get_LeftChild())
            self.preOrderTraversal(self.__RobotData[currentPosition].get_RightChild())
            print()


    def test(self):
        print(self.__RobotData[23].get_DataValue())
        print(len(self.__RobotData))

if __name__ == '__main__':
    robot = RobotTree(25)
    robot.OutputData()
    file = open('SEARCHTREE.txt', 'r')
    for line in file:
        line = line.strip().split(',')
        robot.AddToRobotData(line[0], line[1], line[2])
    file.close()
    robot.OutputData()
    robot.preOrderTraversal(0)
