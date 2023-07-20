def name():
    return "Pancake sort"

def sort(arr):
    cur = len(arr)
    while cur > 1:
        mi = arr.index(max(arr[0:cur]))
        arr = arr[mi::-1] + arr[mi + 1 : len(arr)]
        arr = arr[cur - 1 :: -1] + arr[cur : len(arr)]
        cur -= 1
    return arr
