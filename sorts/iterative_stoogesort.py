def name():
    return "Iterative stooge sort"

def sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        l, h = stack.pop()
        if l >= h:
            continue
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            stack.append((l, h - t))
            stack.append((l + t, h))
            stack.append((l, h - t))
    return arr
