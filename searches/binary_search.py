def name():
    return "Binary search"

def search(items: list, looking_for):
    low = 0
    high = len(items) - 1
    idx = 0
    while low <= high:
        idx = (high + low) // 2
        if items[idx] < looking_for:
            low = idx + 1
        elif items[idx] > looking_for:
            high = idx - 1
        else:
            return idx
    return False

