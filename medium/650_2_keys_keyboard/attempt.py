## Kaden Bilyeu (Bikatr7)
## 2024-08-19
## 650. 2 Keys Keyboard (Medium)

## Description

## There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step.
## * Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
## * Paste: You can paste the characters which are copied last time.
## Given an integer n, return the minimum number of operations to get n 'A' on the screen.

## Example 1
## Input: n = 3
## Output: 3
## Explanation: Initially, we have one character 'A' on the screen.
## In step 1, we use Copy All operation.
## In step 2, we use Paste operation to get 'AA'.
## In step 3, we use Paste operation to get 'AAA'.

## Example 2
## Input: n = 1
## Output: 0

## Constraints

## 1 <= n <= 1000

## Topics: Math, Dynamic Programming

## Hints:
## * How many characters may be there in the clipboard at the last step if n=3? n=7? n= 10? n = 24?

class Solution:
    def minSteps(self, n):
        if(n == 1): return 0
        for i in range(2, int(n**0.5) + 1):
            if(n % i == 0): return i + self.minSteps(n // i)
        return n
    
## Submission Code (Without my way of coding):
class Solution:
    def minSteps(self, n):
        if n == 1: return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return i + self.minSteps(n // i)
        return n
