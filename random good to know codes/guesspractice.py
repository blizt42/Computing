import random as ran
def validate3dNumber(number):
    nonDigit = 0
    not3 = 0
    notSize = 0
    for char in number:
        if not char.isdigit():
            nonDigit += 1
            break
    if nonDigit != 0:
        print('Not a proper number!')
    else:
        if len(number) != 3:
            print('Number is not 3-digit')
            not3 = 1
        if int(number) <= 99 or int(number) >= 1000:
            print('Number is not within 100  to 999')
            notSize = 1
        if not3 == 0 and notSize == 0:
            return True
        else:
            return False

#main
guessNumber = ran.randint(100, 999)
print('You have ten tries to guess a 3-digit number')
tries = 1
while tries <= 10:
    print('Try number {0}'.format(tries))
    number = input('Enter a number')
    if validate3dNumber(number):
        if int(number) == guessNumber:
            print('You guessed the number correctly in {0} guesses!'.format(tries))
            break
        if int(number) < guessNumber:
            print('Too Low')
            tries += 1
        if int(number) > guessNumber:
            print('Too high')
            tries += 1
    else:
        print('invalid number, try again')
if tries == 11:
    print('Sorry you have reached the maximum of 10 guesses!',
          '\nThe correct number is {0}'.format(guessNumber))









