# def binToDen(binNum):
#     placeValue = []
#     for i in range(len(binNum)-1, -1, -1):
#         placeValue.append(2**i)
# ##    print(placeValue)
#     total = 0
#     for i in range(len(binNum)):
#         total = total +int(binNum[i])*placeValue[i]
#     return total
#
# def denToBin(denNum):
#     binNum = ''
#     while int(denNum) != 0:
#         rem = int(denNum) % 2
#         binNum = str(rem) + binNum
#         denNum = int(denNum)//2
#     return binNum

#print(debToBin('8'))

#Qns 3
def hexToDen(hexNum):
    hexValue = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex = list(hexNum)
    total = 0
    for i in range(len(hexNum)):
        for d in range(len(hexValue)):
            if hexValue[d] == hex[i]:
                value = d
                #print('value', value)
                break
        power = (len(hexNum) -(i+1))
        #print('power', power)
        total += (int(value)*16**int(power))
        #print(total)

    return total

#Qn4
def denToHex(denNum):
    hexNum = ''
    hexValue = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while int(denNum) != 0:
        rem = int(denNum) % 16
        for i in range(len(hexValue)):
            if i == rem:
                rem = hexValue[i]
                print(rem)
        hexNum = str(rem) + hexNum
        print('hexnum', hexNum)
        denNum = int(denNum)//16
    return hexNum
#print(denToHex(1234467))

print(hexToDen('A4'))

