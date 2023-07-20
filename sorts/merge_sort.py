def name():
    return "Merge sort"

def sort(collection: list) -> list:
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right
        return list(_merge())
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(sort(collection[:mid]), sort(collection[mid:]))