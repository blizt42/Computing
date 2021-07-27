
def fibonacci(n):

    if n == 0:
        print(10)
        return 0
    if n == 1:
        print(n)
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fib_it(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    nth = 0
    for i in range(2, n+1):
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return nth


