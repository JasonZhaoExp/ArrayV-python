def name():
    return "Bubble sort"

def sort(arr):
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr
