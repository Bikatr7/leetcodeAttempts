## Kaden Bilyeu (Bikatr7)
## 2024-09-03
## 1945. Sum of Digits of String After Convert (Easy)

## Description:
## You are given a string s consisting of lowercase English letters, and an integer k.
## First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
## Return the resulting integer after performing the operations described above.

## Example 1:
## Input: s = "iiii", k = 1
## Output: 36
## Explanation: The operations are as follows:
## - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
## - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
## Thus the resulting integer is 36.

## Example 2:
## Input: s = "leetcode", k = 2
## Output: 6
## Explanation: The operations are as follows:
## - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
## - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
## - Transform #2: 33 ➝ 3 + 3 ➝ 6
## Thus the resulting integer is 6.

## Example 3:
## Input: s = "zbax", k = 2
## Output: 8

## Constraints:
## 1 <= s.length <= 100
## 1 <= k <= 10
## s consists of lowercase English letters.

## Topics: String, Simulation

## Hints:
## Hint 1: First, let's note that after the first transform the value will be at most 100 * 10 which is not much
## Hint 2: After The first transform, we can just do the rest of the transforms by brute force

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = sum(ord(c) - 96 for c in s)
        
        for _ in range(k - 1):
            if (num < 10):
                return num
            num = sum(int(digit) for digit in str(num))
        
        return num
