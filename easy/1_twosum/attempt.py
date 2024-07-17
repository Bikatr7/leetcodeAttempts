## Bikatr7
## 2024-07-16
## 1. Two Sum (Easy)

## Description:

## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.

## Constraints:

## 2 <= nums.length <= 10^4
## -10^9 <= nums[i] <= 10^9
## -10^9 <= target <= 10^9

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Create a dictionary to store the values and their indices
        dict = {}

        for index, num in enumerate(nums):

            ## Check if the difference between the target and the current number is in the dictionary
            if(target - num in dict):
                return [dict[target - num], index]
            
            ## If the difference is not in the dictionary, add the current number and its index to the dictionary
            dict[num] = index
        

## Submission Code:
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if(target - num in dict):
                return [dict[target - num], index]
            dict[num] = index