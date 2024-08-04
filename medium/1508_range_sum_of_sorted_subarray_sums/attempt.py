## Bikatr7
## 2024-08-04
## 1508. Range Sum of Sorted Subarray Sums (Medium)

## Description:

## Given the array nums consisting of n positive integers. You computed the sum of all non-empty continous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
## Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array.
## Since the answer can be a huge number return it modulo 10^9 + 7.

## Constraints:

## n == nums.length
## 1 <= nums.length <= 1000
## 1 <= nums[i] <= 100
## 1 <= left <= right <= n * (n + 1) / 2

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

from typing import List

class Solution:
    def rangeSum(self, nums:List[int], n:int, left:int, right:int) -> int:
        MOD = 10**9 + 7
        max_sum = sum(nums)
        count = [0] * (max_sum + 1)
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                count[s] += 1
        
        for i in range(1, max_sum + 1):
            count[i] += count[i - 1]
        
        result = prev = 0
        for i in range(1, max_sum + 1):
            curr = count[i]
            if(left <= curr):
                result = (result + i * (min(right, curr) - max(left, prev + 1) + 1)) % MOD
            if(curr >= right):
                break
            prev = curr
        
        return result