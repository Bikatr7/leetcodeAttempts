## Bikatr7
## 2024-07-17
## 3. Longest Substring Without Repeating Characters (Medium)

## Description:

## Given a string s, find the length of the longest substring without repeating characters.

## Constraints:

## 0 <= s.length <= 5 * 10^4
## s consists of English letters, digits, symbols and spaces.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:

        last_index = {}
        start = 0
        max_length = 0
        
        ## easily doable with a dictionary

        for i, char in enumerate(s):

            if(char in last_index):
                start = max(start, last_index[char] + 1)

            last_index[char] = i

            max_length = max(max_length, i - start + 1)

        return max_length
    
## Submission Code:
class Solution:
    def lengthOfLongestSubstring(self, s):
        last_index = {}
        start = 0
        max_length = 0
        for i, char in enumerate(s):
            if(char in last_index):
                start = max(start, last_index[char] + 1)
            last_index[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length