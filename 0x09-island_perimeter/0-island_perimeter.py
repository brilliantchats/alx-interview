#!/usr/bin/python3
"""
Calculates the perimeter of an island
"""


def island_perimeter(grid):
    """ Calculate perimeter of a given island - grid """
    perimeter = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i - 1 < 0:
                    perimeter += 1
                elif grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 >= row:
                    perimeter += 1
                elif grid[i + 1][j] == 0:
                    perimeter += 1
                if j - 1 < 0:
                    perimeter += 1
                elif grid[i][j - 1] == 0:
                    perimeter += 1
                if j + 1 >= col:
                    perimeter += 1
                elif grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
