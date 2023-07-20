def name():
    return "Odd-even sort"


def sort(input_list: list) -> list:
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(0, len(input_list) - 1, 2):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                is_sorted = False

        for i in range(1, len(input_list) - 1, 2):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                is_sorted = False
    return input_list
