import random
def readfile():
    file = open('MAZE.txt', 'r')
    lines = file.readlines()
    maze = []
    for i in range(len(lines)):
        line = []
        for j in lines[i]:
            if j == '\n':
                continue
            line.append(j)
        maze.append(line)
    file.close()
    return maze

def DisplayMaze(maze):
    for line in maze:
        display = ''
        for char in line:
            display += char + ' '
        print(display)

def generatePrize(maze):
    for line in maze:
        for i in range(len(line)):
            if line[i] == 'P':
                line[i] = '.'
    generated = False
    # tries = 0
    while not generated:
        vert = random.randint(1,8)
        hori = random.randint(1,9)
        if maze[vert][hori] == '.':
            maze[vert][hori] = 'P'
            generated = True
        # tries += 1
        # print(tries)
    return maze

def generatePlayer(maze):
    for line in maze:
        for i in range(len(line)):
            if line[i] == 'O':
                line[i] = '.'
    vert = 5
    hori = 4
    maze[vert][hori] = 'O'
    return maze

def move(maze, dir, prev):
    for vp in range(len(maze)):
        for hp in range(len(maze[vp])):
            if maze[vp][hp] == 'O':
                oldvert = vp
                oldhori = hp

    if dir == '':
        dir = prev
        vert = oldvert
        hori = oldhori
        if dir == None:
            print('No movement made')
            return maze

    if dir == 'U':
        vert = oldvert - 1
        hori = oldhori
    elif dir == 'D':
        vert = oldvert + 1
        hori = oldhori
    elif dir == 'L':
        hori = oldhori - 1
        vert = oldvert
    elif dir == 'R':
        hori = oldhori + 1
        vert = oldvert

    if maze[vert][hori] == 'X':
        print('You have hit a wall, remaining in postion')
        maze[oldvert][oldhori] = 'O'
    else:
        maze[oldvert][oldhori] = '.'
        maze[vert][hori] = 'O'
    return maze

def checkwin(maze):
    for line in maze:
        for char in line:
            if char == 'P':
                return False
    return True

if __name__ == '__main__':
    maze = generatePlayer(generatePrize(readfile()))
    DisplayMaze(maze)
    totalmoves = [None]
    while True:
        dir = input('Enter direction to move to: ')
        listOfdir = ['U', 'D', 'L', 'R', '']
        if dir in listOfdir:
            maze = move(maze, dir, totalmoves[-1])
        else:
            print('Invalid movement. Try again')
            continue
        if dir != '':
            totalmoves.append(dir)
        print('Last move:', totalmoves[-1])
        print()
        if checkwin(maze):
            print('You won!')
            break
        DisplayMaze(maze)
