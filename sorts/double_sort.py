def name():
    return "Double sort"

def sort(lst):
    no_of_elements = len(lst)
    for _ in range(0, int(((no_of_elements - 1) / 2) + 1)):
        for j in range(0, no_of_elements - 1):
            if (lst[j + 1] < lst[j]):
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
            if (lst[no_of_elements - 1 - j] < lst[no_of_elements - 2 - j]):
                temp = lst[no_of_elements - 1 - j]
                lst[no_of_elements - 1 - j] = lst[no_of_elements - 2 - j]
                lst[no_of_elements - 2 - j] = temp
    return lst
