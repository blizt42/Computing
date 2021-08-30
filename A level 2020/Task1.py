def task1_1(string_value):
    h = 0
    for i in range(len(string_value)-1):
        val = 33 * ord(string_value[i])
        h = h + val % 1024
    return h

def task1_2(seed, string_value):
    newString = seed + string_value
    return task1_1(newString)


# print(task1_1("Hello"))
# print(task1_1("Hallo"))
# print(task1_1("Hullo"))

print(task1_2("seed-one", "Hello"))
print(task1_2("seed-two", "Hello"))
print(task1_2("seed-three", "Hello"))

