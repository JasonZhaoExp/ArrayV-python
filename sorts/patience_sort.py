def name():
    return "Patience sort"

from bisect import bisect_left
from functools import total_ordering
from heapq import merge

@total_ordering
class Stack(list):
    def __lt__(self, other):
        return self[-1] < other[-1]

    def __eq__(self, other):
        return self[-1] == other[-1]


def sort(collection: list) -> list:
    stacks: list[Stack] = []
    for element in collection:
        new_stacks = Stack([element])
        i = bisect_left(stacks, new_stacks)
        if i != len(stacks):
            stacks[i].append(element)
        else:
            stacks.append(new_stacks)
    collection[:] = merge(*(reversed(stack) for stack in stacks))
    return collection
