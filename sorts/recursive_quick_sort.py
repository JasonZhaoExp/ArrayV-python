def name():
    return "Recursive quicksort"

def sort(data: list) -> list:
    if len(data) <= 1:
        return data
    else:
        return [*sort([e for e in data[1:] if e <= data[0]]), data[0], *sort([e for e in data[1:] if e > data[0]]),]