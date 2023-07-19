def name():
    return "Recursive selection sort"

def sort(array, n=None):
    if n is None:
        n = len(array)
    if n <= 1:
        return array
    max_index = 0
    for i in range(1, n):
        if array[i] > array[max_index]:
            max_index = i
    array[max_index], array[n - 1] = array[n - 1], array[max_index]
    sort(array, n - 1)
    return array
