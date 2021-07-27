import random as ran
list = [['BEN01',120],['MAC12',93],['SAM20',187],['ACE07',145]] # part 1

#userID = input('Enter a usernme')
#part 2
def findUser():
    found = False
    for i in list:
        if i[0] == userID:
            print('PLayer found in game')
            found = True
            break
    if not found:
        list.append([userID,0])
        print('New player added')

#part 3
def simulation():
    score = ran.randint(50,200)
    for i in list:
        if i[0] == userID:
            if score >= i[1]:
                i[1] = score
                print('New high score for player {0}'.format(i[0]))
                return

#part 4
def display():
    for i in list:
        print('{0:^10}|{1:<8}'.format(i[0], i[1]))

#part 5
while True:
    userID = input('Enter a username')
    if userID == 'XXX':
        print('Closing program')
        break
    else:
        findUser()
        simulation()
        display()
