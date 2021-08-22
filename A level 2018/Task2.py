def QuickSort(Scores):
    QuickSortHelper(Scores, 0, len(Scores)-1)
    return Scores

def QuickSortHelper(Scores, First, Last):
    if First < Last:
        SplitPoint = Partition(Scores, First, Last)
        QuickSortHelper(Scores, First, SplitPoint-1)
        QuickSortHelper(Scores, SplitPoint+1, Last)
    return Scores

def Partition(Scores, First, Last):
    PivotValue = Scores[First]
    LeftMark = First + 1
    RightMark = Last
    Done = False
    while not Done:
        while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
            LeftMark += 1
        while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
            RightMark -= 1
        if RightMark < LeftMark:
            Done = True
        else:
            temp = Scores[LeftMark]
            Scores[LeftMark] = Scores[RightMark]
            Scores[RightMark] = temp

    temp = Scores[First]
    Scores[First] = Scores[RightMark]
    Scores[RightMark] = temp
    return RightMark

def display(scores):
    print(scores)


file = open('SCORES.txt', 'r')
scores =[]
for line in file:
    line = line.strip().split(',')
    for num in line:
        scores.append(int(num))
display(scores)
file.close()
sorted = QuickSort(scores)
display(scores)
