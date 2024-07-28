## Bikatr7
## 2024-07-17
## 5. Longest Palindromic Substring (Medium)

## Description:

## Given a string s, return the longest palindromic substring in s.

## Constraints:

## 1 <= s.length <= 1000
## s consist of only digits and English letters

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

class Solution:
    def longestPalindrome(self, s:str) -> str:

        ## Manacher's algorithm

        ## Transform the original string to avoid even/odd length issues with palindromes
        transformed_str = '#' + '#'.join(s) + '#'
        n = len(transformed_str)
        palindrome_lengths = [0] * n
        center = right_boundary = 0

        for i in range(n):
            mirror = 2 * center - i

            ## If i is within the right boundary, we can probably use the previously computed palindrome length
            if(i < right_boundary):
                palindrome_lengths[i] = min(right_boundary - i, palindrome_lengths[mirror])

            ## Expand around the center 
            while(i + 1 + palindrome_lengths[i] < n and 
                   i - 1 - palindrome_lengths[i] >= 0 and 
                   transformed_str[i + 1 + palindrome_lengths[i]] == transformed_str[i - 1 - palindrome_lengths[i]]):
                palindrome_lengths[i] += 1

            # Update the center and right boundary if the palindrome around expands past the right boundary-
            if(i + palindrome_lengths[i] > right_boundary):
                center = i
                right_boundary = i + palindrome_lengths[i]

        ## Find the maximum length palindrome in the transformed string
        max_length, center_index = max((length, index) for index, length in enumerate(palindrome_lengths))

        start = (center_index - max_length) // 2
        end = (center_index + max_length) // 2
        
        return s[start:end]

## Submission Code:
class Solution:
    def longestPalindrome(self,s):
        t='#'+'#'.join(s)+'#'
        n=len(t)
        p=[0]*n
        c=r=0
        for i in range(n):
            if i<r:p[i]=min(r-i,p[2*c-i])
            while i-1-p[i]>=0 and i+1+p[i]<n and t[i-1-p[i]]==t[i+1+p[i]]:p[i]+=1
            if i+p[i]>r:c,r=i,i+p[i]
        l,c=max((p[i],i) for i in range(n))
        return s[(c-l)//2:(c+l)//2]