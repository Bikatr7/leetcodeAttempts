## Kaden Bilyeu (Bikatr7)
## 2024-08-16
## 624. Maximum Distance in Arrays (Medium)

## Description:

## You are given m arrays, where each array is sorted in ascending order.
## You can pick up two integers from two different arrays (each array picks one) and calculate the distance.
## We define the distance between two integers a and b to be their absolute difference |a - b|.
## Return the maximum distance.

## Example 1:
## Input: arrays = [[1,2,3],[4,5],[1,2,3]]
## Output: 4
## Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

## Example 2:
## Input: arrays = [[1],[1]]
## Output: 0
## Explanation: You can pick up 1 from the first array and 1 from the second array.

## Constraints:

## m == arrays.length
## 2 <= m <= 10^5
## 1 <= arrays[i].length <= 500
## -10^4 <= arrays[i][j] <= 10^4
## arrays[i] is sorted in ascending order.
## There will be at most 10^5 integers in all the arrays.

## Topics: Array, Greedy

from typing import List

class Solution:
    def maxDistance(self, arrays:List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        result = 0
        
        for i in range(1, len(arrays)):
            result = max(result, 
                         abs(arrays[i][-1] - min_val),
                         abs(max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return result