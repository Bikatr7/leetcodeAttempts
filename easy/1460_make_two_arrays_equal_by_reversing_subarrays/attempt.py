## Bikatr7
## 2024-08-03
## 1460. Make Two Arrays Equal by Reversing Sub-arrays (Easy)

## Description:

## You are given two integer arrays of equal length target and arr.
## In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
## Return True if you can make arr equal to target, or False otherwise.

## Constraints:

## target.length == arr.length
## 1 <= target.length <= 1000
## 1 <= target[i] <= 1000
## 1 <= arr[i] <= 1000

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

from typing import List
from collections import Counter

class Solution:
    def canBeEqual(self, target:List[int], arr:List[int]) -> bool:
        return Counter(target) == Counter(arr)
    
## Submission Code:
class Solution:
    def canBeEqual(self, t, a):
        return Counter(t) == Counter(a)
        