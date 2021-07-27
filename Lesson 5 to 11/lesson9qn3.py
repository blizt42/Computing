def pdrome():
    while True:
        x = input('enter a word')
        y = list(reversed(x))
        if list(x) == y:
            print('yes')
        else:
            print('no')
    
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[len(s)-1] and palindrome(s[1: len(s) -1])
    
#print(palindrome('level'))

def ppdrome(s):
    isPalin = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) -1 - i]:
            isPalin = False
    return isPalin
