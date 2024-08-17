## Kaden Bilyeu (Bikatr7)
## 2024-08-17
## 1937. Maximum Number of Points with Cost (Medium)

## Description:

## You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
## To gain points you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
## However, you will lose points if you pick a cell too far from the cell you picked in the previous row.
## For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
## Return the maximum number of points you can achieve.

## abs(x) is defined as:
## x for x >= 0.
## -x for x < 0.

## Example 1:
## Input: points = [[1,2,3],[1,5,1],[3,1,1]]
## Output: 9
## Explanation: The optimal choice of cells is:
## - Pick cell (0, 2) in the first row. Points = 3
## - Pick cell (1, 1) in the second row. Points = 5
## - Pick cell (2, 0) in the third row. Points = 3
## Total points = 3 + 5 + 3 = 11.
## However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from the score.
## Your final score is 11 - 2 = 9.

## Example 2:
## Input: points = [[1,5],[2,3],[4,2]]
## Output: 11
## Explanation: The optimal choice of cells is:
## - Pick cell (0, 1) in the first row. Points = 5
## - Pick cell (1, 1) in the second row. Points = 3
## - Pick cell (2, 0) in the third row. Points = 4
## Total points = 5 + 3 + 4 = 12.
## However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from the score.
## Your final score is 12 - 1 = 11.

## Constraints:
## m == points.length
## n == points[r].length
## 1 <= m, n <= 10^5
## 1 <= m * n <= 10^5
## 0 <= points[r][c] <= 10^5

## Topics: Dynamic Programming, Array

## Hints:

## 1. Try using dynamic programming to solve this problem.
## 2. dp[i][j] is the maximum number of points you can have if points[i][j] is the most recent cell you picked.

class Solution:
    def maxPoints(self, p):
        m, n = len(p), len(p[0])
        
        dp = p[0]
        
        for i in range(1, m):
            left_max = 0
            new_dp = [0] * n
            
            for j in range(n):
                left_max = max(left_max - 1, dp[j])
                new_dp[j] = left_max + p[i][j]

            right_max = 0
            for j in range(n - 1, -1, -1):
                right_max = max(right_max - 1, dp[j])
                new_dp[j] = max(new_dp[j], right_max + p[i][j])
            
            dp = new_dp
        
        return max(dp)
        