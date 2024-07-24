## Bikatr7
## 2024-07-21
## 2191. Sort the Jumbled Numbers (Medium)

## Description:

## You are given 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system.
## mapping[i] = j means digit i should be mapped to digit j in this system.
## The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 < i < 10.
## You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped value of it's elements.
## Elements with the same mapped value should appear in the same relative order as in the input.
## The elements of nums should only be sorted based on their mapped values and not be replaced by them.

## Constraints:

## mapping.length == 10
## 0 <= mapping[i] <= 9
## All the values of mapping[i] are unique.
## 1 <= nums.length <= 3 * 10^4
## 0 <= nums[i] <= 10^9

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def sortJumbled(self, mapping:typing.List[int], nums:typing.List[int]) -> typing.List[int]:
        def get_mapped_value(num:int) -> int:
            if(num == 0):
                return mapping[0]
            result = 0
            power = 1
            while(num):
                digit = num % 10
                result += mapping[digit] * power
                num //= 10
                power *= 10
            return result
        
        mapped_nums = [(get_mapped_value(num), i, num) for i, num in enumerate(nums)]
        mapped_nums.sort()
        return [num for _, _, num in mapped_nums]
    
## Submission Code:
class Solution:
    def sortJumbled(self, mapping, nums):
        def get_mapped_value(num):
            if num == 0:
                return mapping[0]
            result = 0
            power = 1
            while num:
                digit = num % 10
                result += mapping[digit] * power
                num //= 10
                power *= 10
            return result
        
        mapped_nums = [(get_mapped_value(num), i, num) for i, num in enumerate(nums)]
        mapped_nums.sort()
        return [num for _, _, num in mapped_nums]