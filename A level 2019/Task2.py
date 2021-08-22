def encodeString(data):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIGKLMNOPQRSTUVWXY'
    loweralpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'
    encoded = ''
    for char in data:
        if char.isalpha():
            if char.isupper():
                new = alpha.index(char) + 13
                newchar = alpha[new]
                encoded += newchar
            else:
                new = loweralpha.index(char) + 13
                newchar = loweralpha[new]
                encoded += newchar
        else:
            encoded += char
    return encoded

if __name__ == '__main__':
    data = input('Enter a string of characters: ')
    encoded = encodeString(data)
    print('first encode: ', encoded)
    encoded2 = encodeString(encoded)
    print('Second encode: ', encoded2)