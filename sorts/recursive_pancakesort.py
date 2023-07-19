def name():
    return "Recursive pancake sort"

def sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    max_index = find_max_index(arr, n)
    if max_index != n - 1:
        flip(arr, max_index)
        flip(arr, n - 1)
    return sort(arr, n-1)

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
