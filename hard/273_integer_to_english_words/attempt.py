## Bikatr7
## 2024-08-07
## 273. Integer to English Words (Hard)

## Description:

## Convert a non-negative integer num to its English words representation.
## Example 1:
## Input: num = 123
## Output: "One Hundred Twenty Three"

## Example 2:
## Input: num = 12345
## Output: "Twelve Thousand Three Hundred Forty Five"

## Example 3:
## Input: num = 1234567
## Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

## Constraints:

## 0 <= num <= 2^31 - 1

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def to_words(n):
            if n < 20:
                return less_than_twenty[n]
            if n < 100:
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + less_than_twenty[n % 10])
            if n < 1000:
                return less_than_twenty[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + to_words(n % 100))

        result = []
        for i, unit in enumerate(thousands):
            if num % 1000:
                words = to_words(num % 1000)
                if unit:
                    words += ' ' + unit
                result.append(words)
            num //= 1000
            if num == 0:
                break

        return ' '.join(result[::-1])