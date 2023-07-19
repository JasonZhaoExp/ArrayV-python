def name():
    return "Iterative counting sort"

def sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count_arr = [0] * range_val

    for num in arr:
        count_arr[num - min_val] += 1

    sorted_arr = []
    for i in range(range_val):
        sorted_arr.extend([i + min_val] * count_arr[i])

    return sorted_arr
