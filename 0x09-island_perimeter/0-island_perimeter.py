#!/usr/bin/python3
"""Island perimeter task"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if type(grid) != list:
        return 0

    perimeter = 0

    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
