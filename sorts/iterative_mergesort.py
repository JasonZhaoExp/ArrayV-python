def name():
    return "Iterative merge sort"

def sort(arr):
    if len(arr) <= 1:
        return arr
    def merge(left, right):
        merged = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        return merged
    sorted_arrays = [[num] for num in arr]
    while len(sorted_arrays) > 1:
        new_sorted_arrays = []
        for i in range(0, len(sorted_arrays), 2):
            left = sorted_arrays[i]
            right = sorted_arrays[i + 1] if i + 1 < len(sorted_arrays) else []
            new_sorted_arrays.append(merge(left, right))
        sorted_arrays = new_sorted_arrays
    return sorted_arrays[0]
