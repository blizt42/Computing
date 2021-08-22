array = [5,2,3,1,4,10, 9, 6, 7, 8]

def bubbleSort(arr):
    Swapped = True
    while Swapped:
        Swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                Swapped = True
    return arr


def insertionSort(arr):
    for idx in range(1, len(arr)):
        key = arr[idx]
        j = idx - 1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr


# print(bubbleSort(array))
# print(insertionSort(array))