#question 1

def main():
    fname = input('What is the firstname:')
    lname = input('What is the lastname:')

    print(fname[0])
    print(lname[0:7])

    uname = fname[0] + lname[0:7]
    print(uname)
main()
