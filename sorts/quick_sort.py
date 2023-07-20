def name():
    return "Quicksort"

from random import randrange


def sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]
    greater: list[int] = []
    lesser: list[int] = []

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return [*sort(lesser), pivot, *sort(greater)]