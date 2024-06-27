#!/usr/bin/python3
'''Pascal’s triangle'''


def pascal_triangle(n):
    '''Returns a list of lists of integer representing the Pascal’s triangle'''

    if (n <= 0):
        return []

    pascal = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(len(pascal[i]) - 1):
            row.append(pascal[i][j] + pascal[i][j + 1])
        row.append(1)
        pascal.append(row)
    return pascal
