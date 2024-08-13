## Kaden Bilyeu (Bikatr7)
## 2024-08-13
## 40. Combination Sum II (Medium)

## Description:

## Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
## Each number in candidates may only be used once in the combination.
## Note: The solution set must not contain duplicate combinations.

## Example 1:
## Input: candidates = [10,1,2,7,6,1,5], target = 8
## Output:
## [
## [1,1,6],
## [1,2,5],
## [1,7],
## [2,6]
## ]

## Example 2:
## Input: candidates = [2,5,2,1,2], target = 5
## Output:
## [
## [1,2,2],
## [5]

## Constraints:

## 1 <= candidates.length <= 100
## 1 <= candidates[i] <= 50
## 1 <= target <= 30

## Topics: Array, Backtracking

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        length = len(candidates)
        
        def backtrack(start, target, path):
            if target < 1:
                if target == 0:
                    results.append(path[:])
                return
            for i in range(start, length):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return results
    
## Submission Code:
class Solution:
    def combinationSum2(self, c, t):
        c.sort()
        r,n=[],len(c)
        def b(s,t,p):
            if t<1:r.append(p[:])if t==0else 0;return ## Despite the error, this actually works
            for i in range(s,n):
                if i>s and c[i]==c[i-1]:continue
                if c[i]>t:break
                p+=[c[i]];b(i+1,t-c[i],p);p.pop()
        b(0,t,[])
        return r