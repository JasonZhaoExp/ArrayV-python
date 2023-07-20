def name():
    return "Recursive bubble sort"

def sort(list_data: list, length: int = 0) -> list:
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else sort(list_data, length - 1)
