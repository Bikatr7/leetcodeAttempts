## Bikatr7
## 2024-08-02
## 2134. Minimum Swaps to Group All 1's Together (Medium)

## Description:

## A swap is defined as taking two distinct positions in an array and swapping the values in them.
## A circular array is defined as an array where we can consider the first element and the last element to be adjacent.
## Given a binary circular array nums, return the minimum number of swaps needed to group all 1's together at any location.

## Constraints:

## nums <= nums.length <= 10^5
## nums[i] is 0 or 1

import typing

class Solution:
    def minSwaps(self, nums:typing.List[int]) -> int:
        ones_count = sum(nums)
        if(ones_count == 0):
            return 0
        
        length = len(nums)
        nums *= 2
        current_window_sum = sum(nums[:ones_count])
        min_swaps = ones_count - current_window_sum
        
        for i in range(length):
            current_window_sum = current_window_sum - nums[i] + nums[i + ones_count]
            min_swaps = min(min_swaps, ones_count - current_window_sum)
        return min_swaps

## Submission Code:
class Solution:
    def minSwaps(self, l):
        o = sum(l)
        if o == 0: return 0
        n = len(l)
        l *= 2
        c = sum(l[:o])
        m = o - c
        for i in range(n):
            c = c - l[i] + l[i+o]
            m = min(m, o - c)
        return m