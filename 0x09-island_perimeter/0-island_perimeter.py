#!/usr/bin/python3
"""
Calculates the perimeter of an island
"""


def island_perimeter(grid):
    """ Calculate perimeter of a given island - grid """
    perimeter = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
