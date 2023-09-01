#!/usr/bin/python3
"""
    Function island_perimeter()
    Returns the perimeter of an island
"""


def island_perimeter(grid):
    """
        grid is a list of list of integers
            * 0s represent water & 1s represent land
            * Each cell is a sqaure with side length of 1
            * Cells are connected horizontally/vertically (not diagonally)
            * Grid is rectangular, with width and height not exceeding 100
            * The grid is completely surrounded by water
            * Islands do not have "lakes" (water completely inside the island)
            * There is only one island or nothing

    returns:
        the perimeter of the island
    """
    error_msg = "grid must be a list of lists of ints representing an island"
    if type(grid) != list:
        raise TypeError(error_msg)
    for row in grid:
        if type(row) != list:
            raise TypeError(error_msg)
        for column in row:
            if type(column) != int:
                raise TypeError(error_msg)
            if column != 0 and column != 1:
                raise ValueError(
                    "grid must contain only 0s & 1s representing water & land")
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                perimeter += is_edge(grid, row, column)
    return perimeter


def is_edge(grid, row, column):
    """
    Determines if the given cell is on the edge of the island

    parameters:
        grid [list of lists of ints]: represents the island
        row [int]: the index of row for the current cell
        column [int]: the index of column for the current cell

    returns:
        1-4, if the given cell is on an edge, the number of edges
        0, if the cell of land is in the interior of the island
    """
    edge_count = 0
    if row == 0:
        edge_count += 1
    if row == (len(grid) - 1):
        edge_count += 1
    if row != 0 and grid[row - 1][column] == 0:
        edge_count += 1
    if row != (len(grid) - 1) and grid[row + 1][column] == 0:
        edge_count += 1
    if column == 0:
        edge_count += 1
    if column == (len(grid[row]) - 1):
        edge_count += 1
    if column != 0 and grid[row][column - 1] == 0:
        edge_count += 1
    if column != (len(grid[row]) - 1) and grid[row][column + 1] == 0:
        edge_count += 1
    return edge_count
