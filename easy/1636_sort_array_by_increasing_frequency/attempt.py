## Bikatr7
## 2024-07-22
## 1636. Sort Array by Increasing Frequency (Easy)

## Description:

## Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
## Return the sorted array.

## Constraints:

## 1 <= nums.length <= 100
## -100 <= nums[i] <= 100

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

from collections import Counter

class Solution:
    def frequencySort(self, nums:typing.List[int]) -> typing.List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
    
## Submission Code:
class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))