#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers
    representing the Pascal's triangle of n

    Returns an empty list if n <= 0

    Assumption: n is an integer
    """

    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each subsequent row of the triangle
    for i in range(1, n):
        # Each row starts with one
        row = [1]

        # Compute values for the current row based on the previous row
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1) # Each row ends with 1
        triangle.append(row) # Add completed row to triangle

    return triangle # Return Pascal's triangle
