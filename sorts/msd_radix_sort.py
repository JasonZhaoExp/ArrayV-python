def name():
    return "MSD radix sort"

def sort(list_of_ints: list[int]) -> list[int]:
    if not list_of_ints:
        return []
    if min(list_of_ints) < 0:
        raise ValueError("All numbers must be positive")
    most_bits = max(len(bin(x)[2:]) for x in list_of_ints)
    return _msd_radix_sort(list_of_ints, most_bits)

def _msd_radix_sort(list_of_ints: list[int], bit_position: int) -> list[int]:
    if bit_position == 0 or len(list_of_ints) in [0, 1]:
        return list_of_ints
    zeros = []
    ones = []
    for number in list_of_ints:
        if (number >> (bit_position - 1)) & 1:
            ones.append(number)
        else:
            zeros.append(number)
    zeros = _msd_radix_sort(zeros, bit_position - 1)
    ones = _msd_radix_sort(ones, bit_position - 1)
    res = zeros
    res.extend(ones)
    return res