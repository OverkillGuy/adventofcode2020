from itertools import permutations
from operator import mul as product
from functools import reduce


def day1_sum2(l, target):
    """Finds the 2 numbers that add up to 2020 in list, returning their product

    >>> day1_sum2([1721, 979, 366, 299, 675, 1456], 2020)
    514579
    """
    for i, j in permutations(l, 2):
        if i + j == target:
            return i * j


def day1_sum3(l, target):
    """Finds the 3 numbers that add up to 2020 in list, returning their product

    >>> day1_sum3([1721, 979, 366, 299, 675, 1456], 2020)
    241861950
    """
    for i, j, k in permutations(l, 3):
        if i + j + k == target:
            return i * j * k


def day1_sum(l, target, n):
    """Finds the n numbers that add up to 2020 in list, returning their product

    >>> day1_sum([1721, 979, 366, 299, 675, 1456], 2020, 2)
    514579
    >>> day1_sum([1721, 979, 366, 299, 675, 1456], 2020, 3)
    241861950
    """
    for x in permutations(l, n):
        if sum(x) == target:
            return reduce(product, x)


if __name__ == "__main__":
    with open("input1.txt", "r") as fd:
        data = fd.readlines()
        print(day1_sum2([int(i) for i in data], 2020))
        print(day1_sum3([int(i) for i in data], 2020))
