#!usr/bin/python3
""" Pascal's triangle with Python programming Language"""


def pascal_triangle(n):
    """ FUnction to define an dobtain Pascal's triangle"""

    # Returns an empty list if n is lessthaan or equal to 0
    if n <= 0:
        return []

    triangle = []

    # Generate the rows of the triangle
    for i in range(n):
        row = [1]

        # Now the columns
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # Each row must end with 1
        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle