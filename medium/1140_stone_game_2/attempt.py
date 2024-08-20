## Kaden Bilyeu (Bikatr7)
## 2024-08-19
## 1140. Stone Game II (Medium)

## Description:

## Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 
## The objective of the game is to end with the most stones. 
## Alice and Bob take turns, with Alice starting first. Initially, M = 1.
## On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X).
## The game continues until all the stones have been taken.
## Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

## Example 1:
## Input: piles = [2,7,9,4,4]
## Output: 10
## Explanation: If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

## Example 2:
## Input: piles = [1,2,3,4,5,100]
## Output: 104

## Constraints:

## 1 <= piles.length <= 100
## 1 <= piles[i] <= 104

## Topics: Array, Math, Dynamic Programming, Prefix Sum, Game Theory

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles:List[int]) -> int:
        
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        ## lru cache is complicated, best to think of it as a dict that stores results, but for an entire function so we can save time by not re-running the function with the same inputs

        @lru_cache(None)
        def dp(i:int, m:int) -> int:
            if(i >= n):
                return 0
            if(i + 2 * m >= n):
                return suffix_sum[i]
            
            return max(suffix_sum[i] - dp(i + x, max(m, x)) for x in range(1, min(2 * m, n - i) + 1))
        
        return dp(0, 1)
    
## Submission Code:
from typing import List
from functools import lru_cache
class Solution:
    def stoneGameII(self, p):
        n = len(p)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + p[i]
        @lru_cache(None)
        def dp(i,m):
            if i>=n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            return max(suffix_sum[i] - dp(i + x, max(m, x)) for x in range(1, min(2 * m, n - i) + 1))
        return dp(0, 1)

