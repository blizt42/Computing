def ValidateUserID(ThisUserID):
    if len(ThisUserID) == 9:
        formatcheck = ThisUserID[0:5]
        digits = ThisUserID[5:9]
    else:
        print('UserId more than 9 chars')
        return 1
    if formatcheck == '2015_':
        listdigit = ['0','1','2','3','4','5','6','7','8','9']
        for char in digits:
            if char not in listdigit:
                print('last 4 char is not a digit')
                return 3
    
    else:
        print('Invalid format')
    return 0

ValidateUserID('2015_0987')
ValidateUserID('2015_00987')
ValidateUserID('2015_09A7')
ValidateUserID('2021_0987')
ValidateUserID('2015-0987')
