## Bikatr7
## 2024-07-21
## 4. Median of Two Sorted Arrays (Hard)

## Description:

## Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
## The overall run time complexity should be O(log(m + n)).

## Constraints:

## nums1.length == m
## nums2.length == n
## 0 <= m <= 1000
## 0 <= n <= 1000
## 1 <= m + n <= 2000
## -10^6 <= nums1[i], nums2[i] <= 10^6

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def findMedianSortedArrays(self, nums1:typing.List[int], nums2:typing.List[int]) -> float:
        
        ## rotate the arrays so that nums1 is the smaller array
        if(len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        low, high = 0, m

        ## can use a binary search to find median
        while(low <= high):
            partition_1 = (low + high) // 2
            partition_2 = (m + n + 1) // 2 - partition_1

            max_left_x = float('-inf') if partition_1 == 0 else nums1[partition_1 - 1]
            max_left_y = float('-inf') if partition_2 == 0 else nums2[partition_2 - 1]

            min_right_x = float('inf') if partition_2 == n else nums2[partition_2]
            min_right_y = float('inf') if partition_1 == m else nums1[partition_1]

            ## check if the partition is correct
            if(max_left_x <= min_right_x and max_left_y <= min_right_y):
                if((m + n) % 2 == 0):
                    return (max(max_left_x, max_left_y) + min(min_right_y, min_right_x)) / 2
                else:
                    return max(max_left_x, max_left_y)
                
            elif(max_left_x > min_right_x):
                high = partition_1 - 1

            else:
                low = partition_1 + 1

## Submission Code:
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            partition_1 = (low + high) // 2
            partition_2 = (m + n + 1) // 2 - partition_1
            max_left_x = float('-inf') if partition_1 == 0 else nums1[partition_1 - 1]
            max_left_y = float('-inf') if partition_2 == 0 else nums2[partition_2 - 1]
            min_right_x = float('inf') if partition_2 == n else nums2[partition_2]
            min_right_y = float('inf') if partition_1 == m else nums1[partition_1]
            if max_left_x <= min_right_x and max_left_y <= min_right_y:
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_y, min_right_x)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_x:
                high = partition_1 - 1
            else:
                low = partition_1 + 1