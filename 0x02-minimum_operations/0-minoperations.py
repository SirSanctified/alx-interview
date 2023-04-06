#!/usr/bin/env python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): Number of characters

    Returns:
        int: Fewest number of operations needed to result in exactly n H
        characters in the file
    """
    if n <= 1:
        return 0

    i: int = 2
    count: int = 0

    while i <= n:
        if n % i == 0:
            count += i
            n /= i
        else:
            i += 1

    return count


if __name__ == '__main__':
    n: int = 4
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))

    n: int = 12
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))
