def name():
    return "Recursive merge sort"

def sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    left_half = sort(left_half)
    right_half = sort(right_half)
    result = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result
    
