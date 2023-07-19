def name():
    return "Recursive cycle sort"

def sort(arr, cycleStart=0, writes=0):
    if cycleStart == len(arr) - 1:
        return arr

    item = arr[cycleStart]
    pos = cycleStart
    for i in range(cycleStart + 1, len(arr)):
        if arr[i] < item:
            pos += 1
    if pos != cycleStart:
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
        return sort(arr, cycleStart, writes)

    while pos != cycleStart:
        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

    return sort(arr, cycleStart + 1, writes)
