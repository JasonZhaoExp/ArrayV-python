def name():
    return "Recursive shell sort"

def sort(arr, gap=None):
    if gap is None:
        gap = len(arr) // 2
    if gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        return sort(arr, gap // 2)
    else:
        return arr