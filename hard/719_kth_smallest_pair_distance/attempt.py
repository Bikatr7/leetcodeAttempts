## Kaden Bilyeu (Bikatr7)
## 2024-08-14
## 719. Find K-th Smallest Pair Distance (Hard)

## Description

## The distance of a pair of integers a and b is defined as the absolute difference between a and b.
## Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

## Example 1:
## Input: nums = [1,3,1], k = 1
## Output: 0
## Explanation: Here are all the pairs:
## (1,3) -> 2
## (1,1) -> 0
## (3,1) -> 2
## Then the 1st smallest distance pair is (1,1), and its distance is 0.

## Example 2:
## Input: nums = [1,1,1], k = 2
## Output: 0

## Example 3:
## Input: nums = [1,6,1], k = 3
## Output: 5

## Constraints:
## n == nums.length
## 2 <= n <= 10^4
## 0 <= nums[i] <= 10^6
## 1 <= k <= n * (n - 1) / 2

## Topics: Array, Two Pointers, Binary Search, Sorting

## Hint 1: Binary search for the answer. How can you check how many pairs have distance less than or equal to x?

from typing import List

class Solution:
    def smallestDistancePair(self, nums:List[int], k:int) -> int:
        nums.sort()
        n = len(nums)
        
        def count_pairs(mid):
            count = left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low