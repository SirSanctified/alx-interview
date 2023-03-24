#!/usr/bin/python3
"""
Module that contains a function to generate the pascal triangle
"""

def pascal_triangle(n:int) -> list:
    """
    returns list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (int): size of the triangle

    Returns:
        list: the list of lists containing values for the pascal's triangle
    """
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
