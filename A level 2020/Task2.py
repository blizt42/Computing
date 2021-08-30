from random import randint

# Task 2.1
def task2_1(filename, quantity, maximum):
    listOfnum = []
    count = 1
    while count <= quantity:
        num = randint(0, maximum)
        listOfnum.append(num)
        count += 1
    print(len(listOfnum))
    file = open(filename, 'a')
    for num in listOfnum:
        file.write(str(num)+'\n')
    file.close()

# Task 2.2
def task2_2(list_of_integers):
    if len(list_of_integers) > 1:
        mid = len(list_of_integers) // 2
        left = list_of_integers[:mid]
        right = list_of_integers[mid:]

        task2_2(left)
        task2_2(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_of_integers[k] = left[i]
                i += 1
            else:
                list_of_integers[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list_of_integers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_of_integers[k] = right[j]
            j += 1
            k += 1

    return list_of_integers

# Task 2.3
def task2_3(filename_in, filename_out):
    infile = open(filename_in, 'r')
    list_of_integers = []
    for num in infile:
        num = int(num.strip())
        list_of_integers.append(num)
    infile.close()

    sortedlist = task2_2(list_of_integers)

    outfile = open(filename_out, 'w')
    for num in sortedlist:
        outfile.write(str(num) + '\n')
    outfile.close()



# task2_1('randomnumbers.txt', 1000, 5000)
# print(task2_2([56,25,4,98,0,18,4,5,7,0]))
task2_3('randomnumbers.txt', 'sortednumbers.txt')
