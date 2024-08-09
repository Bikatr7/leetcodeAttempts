## Bikatr7
## 2024-08-09
## 840. Magic Squares In Grid (Medium)

## Description:

## A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
## Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there? 
## Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

## Example 1:
## Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
## Output: 1

## Example 2:
## Input: grid = [[8]]
## Output: 0

## Constraints:

## row == grid.length
## col == grid[i].length
## 1 <= row, col <= 10
## 0 <= grid[i][j] <= 15

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid:List[List[int]]) -> int:
        def is_magic(i: int, j: int) -> bool:
            if grid[i+1][j+1] != 5:
                return False

            s = set()
            for di in range(3):
                for dj in range(3):
                    num = grid[i+di][j+dj]
                    if num < 1 or num > 9 or num in s:
                        return False
                    s.add(num)
            
            return (grid[i][j] + grid[i][j+1] + grid[i][j+2] == 15 and
                    grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == 15 and
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 and
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15 and
                    grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == 15)

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        return sum(is_magic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2))