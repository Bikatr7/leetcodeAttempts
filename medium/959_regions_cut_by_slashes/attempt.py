## Bikatr7
## 2024-08-10
## 959. Regions Cut By Slashes (Medium)

## Description:

## An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '.
## These characters divide the square into contiguous regions.
## Given the grid grid represented as a string array, return the number of regions.
## Note that backslash characters are escaped, so a '\' is represented as '\\'.

## Example 1:
## Input: grid = [" /","/ "]
## Output: 2

## Example 2:
## Input: grid = [" /","  "]
## Output: 1

## Example 3:
## Input: grid = ["/\\","\\/"]
## Output: 5

## Constraints:

## n == grid.length == grid[i].length
## 1 <= n <= 30
## grid[i][j] is either '/', '\', or ' '.

from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range((n + 1) * (n + 1)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        count = 1 
        
        for i in range(n + 1):
            union(0, i)
            union(0, i * (n + 1))
            union(0, (n + 1) * n + i)
            union(0, (n + 1) * i + n)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    if find((i + 1) * (n + 1) + j) == find(i * (n + 1) + j + 1):
                        count += 1
                    union((i + 1) * (n + 1) + j, i * (n + 1) + j + 1)
                elif grid[i][j] == '\\':
                    if find(i * (n + 1) + j) == find((i + 1) * (n + 1) + j + 1):
                        count += 1
                    union(i * (n + 1) + j, (i + 1) * (n + 1) + j + 1)
        
        return count