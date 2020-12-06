import re
from collections import Counter


def check_password(count_min, count_max, letter, candidate):
    """Validates candidate password validates min <= n <= max count of letter

    >>> check_password(1,3,'a','abcde')
    True
    >>> check_password(1,3,'b','cdefg')
    False
    >>> check_password(2,9,'c','ccccccccc')
    True"""
    count = Counter(candidate)
    return count_min <= count[letter] <= count_max


def day2_passcount(l):
    """Count how many passwords are valid given rules

    >>> day2_passcount([(1,3,"a","abcde"), (1,3,"b","cdefg"),(2,9,"c","ccccccccc")])
    2
    """
    return sum(
        check_password(c_min, c_max, let, passwd) for c_min, c_max, let, passwd in l
    )


def check_password2(first, second, letter, candidate):
    """Validates candidate password uses either first or second letter to pass

    >>> check_password2(1,3,'a','abcde')
    True
    >>> check_password2(1,3,'b','cdefg')
    False
    >>> check_password2(2,9,'c','ccccccccc')
    False"""
    return (candidate[first - 1] == letter) ^ (candidate[second - 1] == letter)


def day2_passcount2(l):
    """Count how many passwords are valid given rules

    >>> day2_passcount2([(1,3,"a","abcde"), (1,3,"b","cdefg"),(2,9,"c","ccccccccc")])
    1
    """
    return sum(
        check_password2(first, second, let, passwd) for first, second, let, passwd in l
    )


if __name__ == "__main__":
    regex = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")
    inputs = []
    with open("input2.txt", "r") as fd:
        for line in fd.readlines():
            cmin, cmax, l, p = re.match(regex, line).groups(0)
            inputs.append((int(cmin), int(cmax), l, p))
    print(day2_passcount(inputs))
    print(day2_passcount2(inputs))
