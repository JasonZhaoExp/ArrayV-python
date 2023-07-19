def name():
    return "Iterative strand sort"

def sort(arr):
    result = []
    while arr:
        sublist = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] > sublist[-1]:
                sublist.append(arr.pop(i))
            else:
                i += 1
        result = merge(result, sublist)
    return result

def merge(a, b):
    merged = []
    while a and b:
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    merged.extend(a + b)
    return merged
