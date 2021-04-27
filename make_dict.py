##def make_dict(mylist):
##    oneDict = dict()
##    for key in mylist:
##        oneDict[key] = None
##    return oneDict
##
##print(make_dict(['brave', 'calm', 'delightful', 'eager', 'faithful', 'gentle', 'happy', 'obedient', 'thankful', 'victorious', 'witty', 'zealous']))

def findDivisor(n1, n2):
    divisorTup = ()
    for i in range(1, min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0:
            divisorTup = divisorTup + (i,)
        return divisorTup
print(findDivisor(100, 200))

def findExtremeDivisor(n1, n2):
    minVal, maxVal = (None, None)
    for i in range(2, min(n1,n2)+1):
        if minVal == None or i < minVal:
            minVal = i
        if maxVal == None or i > maxVal:
            maxVal = i
    return (minVal, maxVal)
print(findExtremeDivisor(100,200))
