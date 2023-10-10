def name():
    return "Strand sort"

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list


def sort(arr):
    if len(arr) <= 1:
        return arr

    sorted_list = []
    sublist = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            sublist.append(arr[i])
        else:
            sorted_list = merge_sorted_lists(sorted_list, sublist)
            sublist = [arr[i]]

    sorted_list = merge_sorted_lists(sorted_list, sublist)

    return sorted_list