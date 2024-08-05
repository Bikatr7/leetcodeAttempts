## Bikatr7
## 2024-08-05
## 2053. Kth Distinct String in an Array (Easy)

## Description:

## A distinct string is a string that is present only once in an array
## Given an array of strings arr, and and integer k, return the kth distinct string present in arr.
## If there are fewer than k distinct strings, return an empty string "".
## Note that the strings are considered in the order in which they appear in the array.

## Constraints:

## 1 <= k <= arr.length <= 1000
## 1 <= arr[i].length <= 5
## arr[i] consists of lowercase English letters.

from typing import List

class Solution:
    def kthDistinct(self, arr:List[str], k:int) -> str:
        count = {}
        order = []
        
        for s in arr:
            if(s not in count):
                count[s] = 1
                order.append(s)
            else:
                count[s] += 1
        
        distinct = 0

        for s in order:
            if(count[s] == 1):
                distinct += 1
                if(distinct == k):
                    return s
        
        return ""
        
## Submission Code:
class Solution:
    def kthDistinct(self, a, k):
        c = {}
        o = []
        for s in a:
            if(s not in c):
                c[s] = 1
                o.append(s)
            else:
                c[s] += 1
        
        d = 0
        for s in o:
            if(c[s] == 1):
                d += 1
                if(d == k):
                    return s
        return ""