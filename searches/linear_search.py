def name():
    return "Linear search"

def search(items: list, looking_for):
    for idx, item in enumerate(items):
        if looking_for == item:
            return idx
        else:
            return False