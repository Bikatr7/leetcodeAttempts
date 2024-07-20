## Bikatr7
## 2024-07-20
## 1605. Find Valid Matrix Given Row and Column Sums (Medium)

## Description:

## You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.
## Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.
## Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

## Constraints:
## 1 <= rowSum.length, colSum.length <= 500
## 0 <= rowSum[i], colSum[i] <= 10^8
## sum(rowSum) == sum(colSum)

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def restoreMatrix(self, rowSum:typing.List[int], colSum:typing.List[int]) -> typing.List[typing.List[int]]:
      
        row, col = len(rowSum), len(colSum)

        matrix = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]

        return matrix
    
## Submission Code:
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        row, col = len(rowSum), len(colSum)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
