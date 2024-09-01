## Kaden Bilyeu (Bikatr7)
## 2024-08-31
## 6. Zigzag Conversion (Medium)

## Description:
## The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
## P   A   H   N
## A P L S I I G
## Y   I   R
## And then read line by line: "PAHNAPLSIIGYIR"
## Write the code that will take a string and make this conversion given a number of rows.

## Example 1:
## Input: s = "PAYPALISHIRING", numRows = 3
## Output: "PAHNAPLSIIGYIR"

## Example 2:
## Input: s = "PAYPALISHIRING", numRows = 4
## Output: "PINALSIGYAHRPI"
## Explanation:
## P     I    N
## A   L S  I G
## Y A   H R
## P     I

## Example 3:
## Input: s = "A", numRows = 1
## Output: "A"

## Constraints:
## 1 <= s.length <= 1000
## s consists of English letters (lower-case and upper-case), ',' and '.'.
## 1 <= numRows <= 1000

## Topics: String

class Solution:
    def convert(self, s, numRows):
        if(numRows == 1 or numRows >= len(s)):
            return s

        rows = [''] * numRows
        current_row = 0
        step = 1

        for char in s:
            rows[current_row] += char
            
            if(current_row == 0):
                step = 1
            elif(current_row == numRows - 1):
                step = -1
            
            current_row += step

        return ''.join(rows)
