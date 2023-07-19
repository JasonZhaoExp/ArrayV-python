def name():
    return "Recursive comb sort"

def sort(arr, gap=None, swapped=True):
    if gap is None:
        gap = len(arr)
    shrink = 1.3

    if gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

        return sort(arr, gap, swapped)
    else:
        return arr
