## Kaden Bilyeu (Bikatr7)
## 2024-08-18
## 264. Ugly Number II (Medium)

## Description:

## An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
## Given an integer n, return the nth ugly number.

## Example 1:
## Input: n = 10
## Output: 12
## Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

## Example 2:
## Input: n = 1
## Output: 1
## Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

## Constraints:

## 1 <= n <= 1690

## Topics: Hash Table, Math, Dynamic Programming, Heap (Priority Queue)

## Hints:

## 1. The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
## 2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
## 3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
## 4. Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        for _ in range(1, n):
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            if(umin == u2):
                i2 += 1
            if(umin == u3):
                i3 += 1
            if(umin == u5):
                i5 += 1
            ugly.append(umin)
        return ugly[-1]