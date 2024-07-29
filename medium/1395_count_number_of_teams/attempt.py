## Bikatr7
## 2024-07-29
## 1395. Count Number of Teams (Medium)

## Description:

## There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
## You have to form a team of 3 soldiers amongst them under the following rules:
## Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
## A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
## Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

## Constraints:

## n == rating.length
## 3 <= n <= 1000
## 1 <= rating[i] <= 10^5
## All the integers in rating are unique.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()
## For further speed boosts you can obfuscate the variable names
import typing

class Solution:
    def numTeams(self, rating:typing.List[int]) -> int:
        def update(index:int, value:str) -> None:
            tree_len = len(tree)
            while(index < tree_len):
                tree[index] += value
                index += index & -index

        def query(index:int) -> int:
            total = 0
            while(index > 0):
                total += tree[index]
                index -= index & -index
            return total
        
        n = len(rating)
        sorted_rating = sorted(set(rating))

        rank = {r: i + 1 for i, r in enumerate(sorted_rating)}
        tree = [0] * (n + 1)

        left_smaller = [0] * n
        left_larger = [0] * n

        for i, r in enumerate(rating):
            left_smaller[i] = query(rank[r] - 1)
            left_larger[i] = i - query(rank[r])
            update(rank[r], 1)

        tree = [0] * (n + 1)
        count = 0

        for i in range(n - 1, -1, -1):
            right_smaller = query(rank[rating[i]] - 1)
            right_larger = n - 1 - i - query(rank[rating[i]])
            count += left_smaller[i] * right_larger + left_larger[i] * right_smaller
            update(rank[rating[i]], 1)

        return count
    

