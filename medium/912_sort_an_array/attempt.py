## Bikatr7
## 2024-07-25
## 912. Sort an Array (Medium)

## Description:

## Given an array of integers nums, sort the array in ascending order and return it.
## You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

## Constraints:

## 1 <= nums.length <= 5 * 10^4
## -5 * 10^4 <= nums[i] <= 5 * 10^4

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def sortArray(self, nums:typing.List[int]) -> typing.List[int]:
        def merge_sort(start:int, end:int) -> None:
            if(end - start <= 1):
                return
            
            mid = (start + end) // 2
            
            merge_sort(start, mid)
            merge_sort(mid, end)
            
            left, right = start, mid
            
            temp = []
            
            while(left < mid and right < end):
                if(nums[left] <= nums[right]):
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            temp.extend(nums[left:mid])
            temp.extend(nums[right:end])
            nums[start:end] = temp
        
        merge_sort(0, len(nums))
        
        return nums
    
## Submission Code:
class Solution:
    def sortArray(self, nums):
        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            left, right = start, mid
            temp = []
            while left < mid and right < end:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            temp.extend(nums[left:mid])
            temp.extend(nums[right:end])
            nums[start:end] = temp
        merge_sort(0, len(nums))
        return nums