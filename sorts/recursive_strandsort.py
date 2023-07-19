def name():
    return "Recursive strand sort"

def sort(arr):
    if not arr:
        return []
    sublist = [arr.pop(0)]
    i = 0
    while i < len(arr):
        if arr[i] > sublist[-1]:
            sublist.append(arr.pop(i))
        else:
            i += 1
    return merge(sublist, sort(arr))

def merge(a, b):
    merged = []
    while a and b:
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    merged.extend(a + b)
    return merged
