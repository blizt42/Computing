# Task 1.1

def bubbleSort(arr):
    for i in range(len(arr)-2):
        posn = 0
        noswap = True
        while posn != len(arr)-1:
            if arr[posn] > arr[posn+1]:
                noswap = False
                temp = arr[posn]
                arr[posn] = arr[posn+1]
                arr[posn+1] = temp
            posn += 1
        if noswap == True:
            return arr
    return arr

def binary(arr, low, high, title):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == title:
            return True
        elif arr[mid] < title:
            low = mid + 1
        else:
            high = mid - 1
    return False


file = open('MOVIES.txt', 'r')
movies = []
for line in file:
    movie = line.strip().split(' ')
    moviename = ''
    for i in range(len(movie)-1):
        moviename += f'{movie[i]} '
    movies = movies + [moviename[:-1]]

find = input('Enter movie to find: ')
movies = bubbleSort(movies)
print(binary(movies, 0, len(movies), find))



