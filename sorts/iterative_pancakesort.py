def name():
    return "Iterative pancake sort"

def sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(arr, curr_size)
        if max_index != curr_size - 1:
            flip(arr, max_index)
            flip(arr, curr_size - 1)
    return arr

def find_max_index(arr, n):
    max_index = 0
    for i in range(n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def flip(arr, idx):
    start = 0
    while start < idx:
        arr[start], arr[idx] = arr[idx], arr[start]
        start += 1
        idx -= 1
