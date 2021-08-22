def findHighest(tl):
    highest = 0.0
    for data in tl:
        if float(data[3]) > highest:
            highest = float(data[3])
    return highest

def findLowest(tl):
    lowest = 1000.0
    for data in tl:
        if float(data[3]) < lowest:
            lowest = float(data[3])
    if lowest == 1000.0:
        return 'No data found'
    return lowest

def findLargeRange(tl):
    largest = 0.0
    for idx in range(len(tl)-1):
        front = float(tl[idx][3])
        end = float(tl[idx+1][3])
        trange = abs(end - front)
        if trange > largest:
            largest = trange
            data = [tl[idx], tl[idx+1]]
    #print(data)
    return str(largest)[:3] , data[1][0]

def findSmallRange(tl):
    smallest = 1000.0
    for idx in range(len(tl) - 1):
        front = float(tl[idx][3])
        end = float(tl[idx + 1][3])
        trange = abs(end - front)
        if trange < smallest:
            smallest = trange
            data = [tl[idx], tl[idx+1]]

    if smallest == 1000.0:
        return 'No data found'
    return smallest, data[1][0]

if __name__ == '__main__':
    file = open('TIDES.txt', 'r')
    tidelist = []
    for line in file:
        line = line.strip().split('\t')
        tidelist.append(line)
    file.close()
    print(findHighest(tidelist))
    print(findLowest(tidelist))
    print(findLargeRange(tidelist))
    print(findSmallRange(tidelist))