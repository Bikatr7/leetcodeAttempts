## Bikatr7
## 2024-07-16
## 9. Palindrome Number

## Description:

## Given an integer x, return true if x is a palindrome, and false otherwise.

## Constraints:

## -231 <= x <= 231 - 1
## Solution must be without converting the integer to a string

## Given my code style it is recommended to submit without any comments, spacing, type hints, or ()

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        ## solve without converting to string
        ## if negative, return False
        if(x < 0):
            return False
        
        if(x < 10):
            return True
        
        ## if last digit is 0, return False
        if(x % 10 == 0):
            return False
        
        ## reverse the number
        reverse = 0

        while(x > reverse):
            reverse = reverse * 10 + x % 10
            x //= 10

        ## if the number is even, return True if x == reverse
        ## if the number is odd, return True if x == reverse // 10
        return x == reverse or x == reverse // 10
    

## Submission Code:
class Solution:
    def isPalindrome(self, x):
        if(x < 0):
            return False
        if(x < 10):
            return True
        if(x % 10 == 0):
            return False
        reverse = 0
        while(x > reverse):
            reverse = reverse * 10 + x % 10
            x //= 10
        return x == reverse or x == reverse // 10