## Bikatr7
## 2024-07-30
## 1653. Minimum Deletions to Make String Balanced (Medium)

## Description:

## You are given a string s consisting only of characters 'a' and 'b'.
## You can delete any number of characters in s to make s balanced.
## s is balanced if there is no pair of indices (i, j) such that i < j and s[i] = 'b' and s[j] = 'a'.
## Return the minimum number of deletions needed to make s balanced.

## Constraints:

## 1 <= s.length <= 10^5
## s[i] is 'a' or 'b'.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

class Solution:
    def minimumDeletions(self,s:str) -> int:
        count_b = deletions = 0
        for char in s:
            if(char < 'b'):
                if(count_b):
                    count_b -= 1
                    deletions += 1
            else:
                count_b += 1

        return deletions

## Submission code:
class Solution:
    def minimumDeletions(self,s):
        b=d=0
        for c in s:
            if c<'b':
                if b:b-=1;d+=1
            else:b+=1
        return d