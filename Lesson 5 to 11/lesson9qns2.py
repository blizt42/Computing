def numbers():
    y =0
    while True:        
        x = input('enter a real number')
        
        if x == '':
            return y
        else:
            y = y + int(x)
    

def read_add():
    number = input('eee')
    if number == '':
        return 0.0
    else:
        return float(number) + read_add()
            
