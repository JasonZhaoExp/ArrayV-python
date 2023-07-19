def name():
    return "Iterative quick sort"

def sort(array):
    stack = [(0, len(array) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = array[(low + high) // 2]
        i, j = low, high
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        stack.append((low, j))
        stack.append((i, high))
    return array