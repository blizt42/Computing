def main():
    
    rate = eval(input('Please enter annualised interest rate:'))
    x = eval(input('Please enter initial investment:'))
    y = x*2
    years = 0
    while x < y:
        x = x*(1+rate/100)**1
        years = years +1

    print('It takes', years, 'years')
main()
