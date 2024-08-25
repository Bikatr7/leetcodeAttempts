## Kaden Bilyeu (Bikatr7)
## 2024-08-23
## 564. Find the Closest Palindrome (Hard)

## Description:

## Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
## The closest is defined as the absolute difference minimized between two integers.

## Example 1:
## Input: n = "123"
## Output: "121"

## Example 2:
## Input: n = "1"
## Output: "0"
## Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

## Constraints:

## 1 <= n.length <= 18
## n consists of only digits.
## n does not have leading zeros.
## n is representing an integer in the range [1, 10^18 - 1].

## Topics: Math, String

## Hints:
## 1. Will brute force work for this problem? Think of something else.
## 2. Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
## 3. Do we have to consider only left half or right half of the string or both?
## 4. Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?

class Solution:
    def nearestPalindromic(self, n:str) -> str:
    
        if(len(n) <= 1):
            return '1' if n == '0' else str(int(n) - 1)
        
        num, length = int(n), len(n)
        half = (length + 1) // 2
        left = int(n[:half])
        
        def make_palindrome(x):
            s = str(x)
            return int(s + (s[-2::-1] if length % 2 else s[::-1]))
        
        candidates = [10**(length - 1) - 1, 10**length + 1]
        candidates.extend(make_palindrome(i) for i in range(left - 1, left + 2))
        
        return str(min((c for c in candidates if c != num), 
                       key=lambda x: (abs(x - num), x)))

## Submission Code:
class Solution:
    def nearestPalindromic(self, n):
        if len(n) <= 1:
            return '1' if n == '0' else str(int(n) - 1)
        num, length = int(n), len(n)
        half = (length + 1) // 2
        left = int(n[:half])
        def make_palindrome(x):
            s = str(x)
            return int(s + (s[-2::-1] if length % 2 else s[::-1]))
        candidates = [10**(length - 1) - 1, 10**length + 1]
        candidates.extend(make_palindrome(i) for i in range(left - 1, left + 2))
        return str(min((c for c in candidates if c != num), 
                       key=lambda x: (abs(x - num), x)))