def name():
    return "Recursive cocktail shaker sort"

def sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr
    
    swapped = False
    for i in range(start, end):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    
    for i in range(end-1, start-1, -1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    
    if swapped:
        return sort(arr, start + 1, end - 1)
    else:
        return arr
