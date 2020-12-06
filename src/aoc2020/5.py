def seat_position(address):
    """
    >>> seat_position("BFFFBBFRRR")
    567
    >>> seat_position("FFFBBBFRRR")
    119
    >>> seat_position("BBFFBBFRLL")
    820
    """
    row, column = address[:-3], address[-3:]
    return seat_id(decode_frontback(row), decode_rightleft(column))


def decode_frontback(address):
    """
    >>> decode_frontback("FBFBBFF")
    44
    >>> decode_frontback("BFFFBBF")
    70
    >>> decode_frontback("FFFBBBF")
    14
    >>> decode_frontback("BBFFBBF")
    102
    """
    binary_string = address.replace("F", "0").replace("B", "1")
    # Decode binary string as int
    # See https://docs.python.org/3.6/library/functions.html#int
    return int(binary_string, 2)


def decode_rightleft(address):
    """
    >>> decode_rightleft("RLR")
    5
    >>> decode_rightleft("RRR")
    7
    >>> decode_rightleft("RLL")
    4
    """
    binary_string = address.replace("L", "0").replace("R", "1")
    # Decode binary string as int
    # See https://docs.python.org/3.6/library/functions.html#int
    return int(binary_string, 2)


def seat_id(row, column):
    return row * 8 + column


def missing_seat(seats):
    """
    >>> missing_seat([3, 5, 6, 7])
    4
    """
    sorted_seats = sorted(seats)
    for before, after in zip(sorted_seats[:-1], sorted_seats[1:]):
        difference = after - before
        if difference != 1:
            return before + 1


if __name__ == "__main__":
    with open("input5.txt", "r") as fd:
        data = fd.readlines()
    seats = [seat_position(i.replace("\n", "")) for i in data]
    print(max(seats))
    print(missing_seat(seats))
