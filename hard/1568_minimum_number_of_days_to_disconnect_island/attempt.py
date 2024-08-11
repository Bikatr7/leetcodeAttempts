## Bikatr7
## 2024-08-11
## 1568. Minimum Number of Days to Disconnect Island (Hard)

## Description:

## You are given an m x n binary grid grid, where 1 represents and 0 represents water. 
## An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.
## The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
## In one day, we are allowed to change any single land cell (1) into a water cell (0).
## Return the minimum number of days to disconnect the grid.

## Example 1:

## Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
## Output: 2
## Explanation: We need at least 2 days to get a disconnected grid. 
## Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

## Example 2:

## Input: grid = [[1,1]]
## Output: 2
## Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

## Constraints:

## m == grid.length
## n == grid[i].length
## 1 <= m, n <= 30
## grid[i][j] is 0 or 1.

## Topics

## Array, Depth-first Search, Breadth-first Search, Matrix, Strongly Connected Component

## Hints

## 1. Return 0 if the grid is already disconnected.
## 2. Return 1 if changing a single land cell can disconnect the grid.
## 3. Otherwise return 2.
## 4. We can disconnect the grid within at most 2 days.

from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int, visited: set) -> None:
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, visited)
        
        def count_islands() -> int:
            visited = set()
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count
        
        def is_bridge(i: int, j: int) -> bool:
            original = grid[i][j]
            grid[i][j] = 0
            islands = count_islands()
            grid[i][j] = original
            return islands != 1
        
        # Check if already disconnected
        if count_islands() != 1:
            return 0
        
        # Check if removing any single cell disconnects the island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and is_bridge(i, j):
                    return 1
        
        return 2