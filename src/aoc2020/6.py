import operator
from functools import reduce


def count_any(answers):
    """
    >>> sorted(list(count_any(['abc'])))
    ['a', 'b', 'c']
    >>> sorted(list(count_any(['a','b','c'])))
    ['a', 'b', 'c']
    >>> sorted(list(count_any(['ab','ac'])))
    ['a', 'b', 'c']
    >>> sorted(list(count_any(['a','a','a','a'])))
    ['a']
    >>> sorted(list(count_any(['b'])))
    ['b']
    """
    return reduce(operator.or_, (set(answers) for answers in answers))


def day6_1(data):
    """
    >>> day6_1("abc\\n\\na\\nb\\nc\\n\\nab\\nac\\n\\na\\na\\na\\na\\n\\nb")
    11
    """
    groups = [group.split("\n") for group in data.split("\n\n")]
    acc = 0
    for group in groups:
        acc += len(count_any(group))
    return acc


def count_all(answers):
    """
    >>> sorted(list(count_all(['abc'])))
    ['a', 'b', 'c']
    >>> sorted(list(count_all(['a','b','c'])))
    []
    >>> sorted(list(count_all(['ab','ac'])))
    ['a']
    >>> sorted(list(count_all(['a','a','a','a'])))
    ['a']
    >>> sorted(list(count_all(['b'])))
    ['b']
    """
    return reduce(operator.and_, (set(answers) for answers in answers))


def day6_2(data):
    """
    >>> day6_2("abc\\n\\na\\nb\\nc\\n\\nab\\nac\\n\\na\\na\\na\\na\\n\\nb\\n\\n")
    6
    """
    groups = [group.split("\n") for group in data.split("\n\n")]
    acc = 0
    for group in groups:
        acc += len(count_all(group))
    return acc


if __name__ == "__main__":
    with open("input6.txt", "r") as fd:
        data = fd.read()
    print(day6_1(data))
    print(day6_2(data))
