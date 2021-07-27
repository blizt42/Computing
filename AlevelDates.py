def display(arr):
    print('\n{:^13}|{:^13}|{:^14}|{:^7}|{:^20}|{:^20}|{:^10}'.format(
        'Date', 'Time', 'Subject Code', 'Paper', 'Subject', 'Type', 'Duration'))
    for paper in arr:
        print('{:^13}|{:^13}|{:^14}|{:^7}|{:^20}|{:^20}|{:^10}'.format(
            paper[0], paper[1], paper[2], paper[3], paper[4], paper[5], paper[6]))
    input('\nPress enter to continue...')

def subject(arr, sub):
    subarray = []
    code = {'1': '9749', '2': '9758', '3': '9569', '4': '8813', '5': '8807'}
    for paper in arr:
        if code[sub] in paper:
            subarray.append(paper)
    display(subarray)

def dates(arr):
    n = len(arr)
    swap = True
    while swap:
        swap = False
        for i in range(n-1):
            date1 = arr[i][0].split('/')
            date2 = arr[i+1][0].split('/')
            if int(date1[1]) == int(date2[1]):
                if int(date1[0]) > int(date2[0]):
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    swap = True
            elif int(date1[1]) > int(date2[1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True
    display(arr)

def duration(arr):
    duraArr = arr
    for paper in duraArr:
        time = ''
        for i in range(len(paper[6])):
            if paper[6][i] == ':':
                time += '.'
            else:
                time += paper[6][i]
        paper[6] = float(time)
    i = 0
    while i <= (len(duraArr)-2):
        if duraArr[i][6] > duraArr[i+1][6]:
            temp = arr[i + 1]
            check = duraArr[i+1]
            j = i
            while j >= 0 and duraArr[j][6] > check[6]:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = temp
        i += 1
    for paper in duraArr:
        time = ''
        for i in range(len(str(paper[6]))):
            temp = str(paper[6])
            if temp[i] == '.':
                time += ':'
            else:
                time += temp[i]
        paper[6] = time + '0'
    display(arr)

def Time(arr):
    for paper in arr:
        start = paper[1].split(' - ')[0]
        paper[1] = paper[1].split(' - ')
        time = ''
        for i in range(len(start)):
            if start[i] == ':':
                time += '.'
            else:
                time += start[i]
        paper[1][0] = float(time)
    am = []
    pm = []
    for paper in arr:
        if paper[1][0] < 12.0:
            am.append(paper)
        else:
            pm.append(paper)
    for paper in am:
        convert = str(paper[1][0])
        time = '0' if len(convert) < 4 else ''
        for i in range(len(convert)):
            if convert[i] == '.':
                time += ':'
            else:
                time += convert[i]
        paper[1][0] = time + '0'
        paper[1] = str(paper[1][0]) + ' - ' + str(paper[1][1])

    for paper in pm:
        convert = str(paper[1][0])
        time = ''
        for i in range(len(convert)):
            if convert[i] == '.':
                time += ':'
            else:
                time += convert[i]
        paper[1][0] = time + '0'
        paper[1] = str(paper[1][0]) + ' - ' + str(paper[1][1])
    print('\nMorning papers:')
    display(am)
    print('\nAfternoon papers:')
    display(pm)

def practical(arr):
    pract = []
    for paper in arr:
        if 'PRACTICAL' in paper[5]:
            pract.append(paper)
    display(pract)

def main():
    array = []
    file = open('AlevelDates.txt', 'r')
    for i in file:
        line = i.strip().split(',')
        array.append(line)
    file.close()
    while True:
        print('''What would you like to do?
        1. View a subject
        2. View by Dates
        3. View by Duration
        4. View by AM and PM
        5. View practical dates''')
        choice = input('Select an option ("X" to leave): ')
        if choice == '1':
            print('''Subjects:
            1. Physics
            2. Math
            3. Computing
            4. Geography
            5. General Paper''')
            sub = input('Select the subject: ')
            subject(array, sub)
        elif choice == '2':
            dates(array)
        elif choice == '3':
            duration(array)
        elif choice == '4':
            Time(array)
        elif choice == '5':
            practical(array)
        elif choice == 'X':
            print('Goodbye...')
            break
        else:
            print('Unknown option, please try again.')

if __name__ == '__main__':
    main()
