def name():
    return "Insertion sort"

def sort(list):
    for idx, value in enumerate(list[1:]):
        tmp_idx = idx
        while idx >= 0 and value < list[idx]:
            list[idx + 1] = list[idx]
            idx -= 1
        if idx != tmp_idx:
            list[idx + 1] = value
    return list
