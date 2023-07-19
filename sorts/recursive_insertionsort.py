def name():
    return "Recursive insertion sort"

def sort(array):
    if len(array) <= 1:
        return array
    first_element = array[0]
    rest_of_array = array[1:]
    sorted_rest = sort(rest_of_array)
    for i in range(len(sorted_rest)):
        if first_element < sorted_rest[i]:
            return sorted_rest[:i] + [first_element] + sorted_rest[i:]
    return sorted_rest + [first_element]