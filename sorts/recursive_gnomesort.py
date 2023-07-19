def name():
    return "Recursive gnome sort"

def sort(arr, i=0):
    if i == len(arr):
        return arr
    if i == 0 or arr[i] >= arr[i - 1]:
        return sort(arr, i + 1)
    else:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        return sort(arr, i - 1)
