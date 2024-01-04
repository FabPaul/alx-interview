#!usr/bin/python3
""" Pascal's triangle with Python programming Language"""


def pascal_triangle(n):
    """ FUnction to define an dobtain Pascal's triangle"""

    # Returns an empty list if n is lessthaan or equal to 0
    if n <= 0:
        return []

    triangle = [[1]]

    # generate values for the new row from the previous one
    for row in range(1, n):
        prev_row = triangle[row - 1]
        new_row = [1]

        for column in range(1, row):
            value = prev_row[column - 1] + prev_row[column]
            new_row.append(value)

        # Add the last element to the new row
        new_row.append(1)

        # Add the mew row to the Pascal's triangle
        triangle.append(new_row)

    return triangle