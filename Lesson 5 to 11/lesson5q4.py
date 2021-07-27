def main():
    acn = input("Enter a few words:")
    x = acn.title()
    for char in x:
        if char.isupper():
            print(char, end="")
main()
    
