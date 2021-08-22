def readfile():
    file = open('STARS.txt', 'r')
    names = []
    steps = []
    lines = file.readlines()
    for i in range(len(lines)):
        if (i+1) % 2 > 0:
            names.append(lines[i].strip())
        else:
            steps.append(lines[i][1:])
    file.close()
    return names, steps

def display(old, new):
    print(f'Last week, {old[0]} was "Star of the week" with {old[1]} steps taken.')
    print(f'This week, {new[0]} is "Star of the week" with {new[1]} steps taken.')

def update(new):
    file = open('STARS.txt', 'w')
    file.write(f'{new[0]}\n')
    file.write(f',{new[1]}')
    file.close()


def main():
    while True:
        try:
            numOfNames = int(input('Enter number of names: '))
            if numOfNames > 10:
                print('Maximum of 10 names allowed, try again')
            else:
                break
        except:
            print('invalid number, try again')
    listOfNames = ['' for i in range(numOfNames)]
    listOfSteps = ['' for i in range(numOfNames)]
    mostSteps = [None, 0]
    for num in range(numOfNames):
        listOfNames[num] = input(f'Enter name number {num}: ')
        while True:
            try:
                listOfSteps[num] = int(input(f'Enter steps taken for {listOfNames[num]}: '))
                break
            except:
                print('invalid number, try again')
        if listOfSteps[num] > mostSteps[1]:
            mostSteps[0] = listOfNames[num]
            mostSteps[1] = listOfSteps[num]

    stars, starSteps = readfile()
    old = [stars[len(stars)-1], starSteps[len(stars)-1]]
    new = [mostSteps[0], mostSteps[1]]
    display(old, new)
    update(new)

if __name__ == '__main__':
    main()





