def main():
    print("this prog. converts F to C")
    fahrenheit = eval(input("what is the fahrenheit temp?"))
    celsius = (fahrenheit-32) * 5/9
    print("it is", celsius, "degrees Celsius.")

main()
