## Kaden Bilyeu (Bikatr7)
## 2024-08-19
## 664. Strange Printer (Hard)

## Description:

## There is a strange printer with the following two special properties:
## 1. The printer can only print a sequence of the same character each time.
## 2. At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
## Given a string s, return the minimum number of turns the printer needed to print it.

## Example 1:
## Input: s = "aaabbb"
## Output: 2
## Explanation: Print "aaa" first and then print "bbb".

## Example 2:
## Input: s = "aba"
## Output: 2
## Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

## Constraints:
## 1 <= s.length <= 100
## s consists of lowercase English letters.

## Topics: String, Dynamic Programming

## I'm bad at this one, absolutely not an optimal solution here

class Solution:
    def strangePrinter(self, s: str) -> int:
        ## Remove consecutive duplicate characters
        ## This optimization reduces the problem size without affecting the result
        s = ''.join(ch for i, ch in enumerate(s) if i == 0 or ch != s[i-1])
        
        n = len(s)
        #
        # #dp[i][j] represents the minimum number of turns to print s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        ## for all possible substring lengths
        for length in range(1, n + 1):
            ## for all possible starting positions for the current length
            for i in range(n - length + 1):
                j = i + length - 1  
                
                ## Initialize with worst case: print each character separately
                dp[i][j] = length
                
                ## Try all possible split points
                for k in range(i, j):
                    ##  Calculate the current number of turns, it's the sum of turns for left and right parts
                    current = dp[i][k] + dp[k+1][j]
                    
                    ## If the characters at k and j are the same,
                    ## we can potentially save one turn
                    if s[k] == s[j]:
                        current -= 1
                    
                    ## Update dp[i][j] with the minimum turns found
                    dp[i][j] = min(dp[i][j], current)
        
        return dp[0][n-1]

## Submission Code:
class Solution:
    def strangePrinter(self, s):
        s = ''.join(ch for i, ch in enumerate(s) if i == 0 or ch != s[i-1])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length
                for k in range(i, j):
                    current = dp[i][k] + dp[k+1][j]
                    if s[k] == s[j]:
                        current -= 1
                    dp[i][j] = min(dp[i][j], current)
        return dp[0][n-1]

        

