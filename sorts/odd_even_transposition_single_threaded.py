def name():
    return "Non-parallelized odd-even transposition sort"

def sort(arr: list) -> list:
    arr_size = len(arr)
    for _ in range(arr_size):
        for i in range(_ % 2, arr_size - 1, 2):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
