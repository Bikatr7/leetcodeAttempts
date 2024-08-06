## Bikatr7
## 2024-08-06
## 3016. Minimum Number of Pushes to Type Word II (Medium)

## Description:

## You are given a string word containing lowercase English letters.
## Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them.
## For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
## It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
## The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
## You need to find the minimum number of times the keys will be pushed to type the string word.
## Return the minimum number of pushes needed to type word after remapping the keys.
## An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

## Constraints:

## 1 <= word.length <= 10^5
## word consists of lowercase English letters.

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for b in word.encode():
            freq[b - 97] += 1
        
        freq.sort(reverse=True)
        
        total = 0
        for i, f in enumerate(freq):
            total += (i // 8 + 1) * f
        
        return total