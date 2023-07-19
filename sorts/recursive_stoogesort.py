def name():
    return "Recursive stooge sort"

def sort(arr, l=0, h=None):
    if h is None:
        h = len(arr) - 1

    if l >= h:
        return arr

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        sort(arr, l, h - t)
        sort(arr, l + t, h)
        sort(arr, l, h - t)

    return arr
