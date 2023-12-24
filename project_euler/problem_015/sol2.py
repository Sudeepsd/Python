"""
https://projecteuler.net/problem=15
Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

    -- --
   |  |  |
    -- --
   |  |  |
    -- --
    
How many such routes are there through a 20x20 grid?
"""

def solution(m: int = 20, n: int = 20) -> int:
    """
    Returns the number of paths possible in a m x n grid starting at top left
    corner going to bottom right corner and being able to move right and down
    only.
    >>> solution(25, 25)
    126410606437752
    >>> solution(23, 23)
    8233430727600
    >>> solution(20, 20)
    37846528820
    >>> solution(15, 15)
    155117520
    >>> solution(1, 1)
    2
    """
    grid = [["" for i in range(0, m + 1)] for j in range(0, n + 1)]
    
    for i in range(0, m + 1):
        grid[i][0] = 1
    for i in range(0, n + 1):
        grid[0][i] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]
    
    return grid[m][n]
    
if __name__ == '__main__':
    print(f"{solution() = }")
