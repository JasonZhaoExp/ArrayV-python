def name():
    return "Recursive odd even sort"

def sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(1, n - 1, 2):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    for i in range(0, n - 1, 2):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return sort(arr, n-1)
