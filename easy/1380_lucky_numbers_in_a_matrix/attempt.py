## Bikatr7
## 2024-07-19
## 1380. Lucky Numbers in a Matrix (Easy)

## Description:

## Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
## A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

## Constraints:

## m == mat.length
## n == mat[i].length
## 1 <= n, m <= 50
## 1 <= matrix[i][j] <= 10^5
## All elements in the matrix are distinct.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

from typing import List

class Solution:
    def luckyNumbers (self, matrix:List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

## Submission Code:
class Solution:
    def luckyNumbers (self, matrix):
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})