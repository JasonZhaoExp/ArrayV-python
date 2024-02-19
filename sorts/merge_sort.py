def name():
    return "Merge sort"

def sort(list: list) -> list:
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right
        return list(_merge())
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    return merge(sort(list[:mid]), sort(list[mid:]))