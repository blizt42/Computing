def main():
    total = 0 #initial total is 0, keep track of sum numbers
    count = 1 #initial count number is 1, count will increase by 2 everytime the loop is repeated
    n = eval(input("Enter an integer n:"))

    while count <= 2*n-1:
        total = total + count
        count = count + 2

    print(total)
    



#qns4C
def main2():
    number = 0 # initial number to get into loop body
    total = 0 # initial total is 0                 
    while number != 999:
        number = eval(input("Enter a number to be added:"))
        total = total + number
    print(total - 999)



#4d
def main3():
    number = eval(input('Enter a whole number:'))
    times = 0
    while number != 1:
        number = number // 2
        times = times + 1
    print(times)

main3()
