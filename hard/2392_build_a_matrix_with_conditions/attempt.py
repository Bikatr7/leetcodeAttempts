## Bikatr7
## 2024-07-21
## 2392. Build a Matrix With Conditions (Hard)

## Description:

## You are given a positive integer k. You are also given
## a 2D integer array rowConditions of size n where rowConditions[i] = [above>i, below>i] and
## a 2D integer array colConditions of size m where colConditions[i] = [left>i, right>i].
## The two arrays contain integers from 1 to k.
## You have to build a k x k matrix that contains each of the integers from 1 to k exactly once, the remaining cells should be filled with zeros.
## The matrix should also satisfy the following conditions:
## THe number above>i, should appear in a row that is strictly above the row at which the number below>i appears for all i from 0 to n-1.
## The number left>i should appear in a column that is strictly to the left of the column at which the number right>i appears for all i from 0 to m-1.
## Return any matrix that satisfies the conditions, if it is possible. Otherwise, return an empty matrix.

## Constraints:

## 2 <= k <= 400
## 1 <= rowConditions.length, colConditions.length <= 10^4
## rowConditions[i].length == colConditions[j].length == 2
## 1 <= above>i, below>i, left>i, right>i <= k
## above>i != below>i
## left>i != right>i

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

from collections import defaultdict

class Solution:
    def buildMatrix(self, k:int, rowConditions:typing.List[typing.List[int]], colConditions:typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
       
        def build_graph(conditions:typing.List[typing.List[int]]) -> typing.Tuple[typing.Dict[int, typing.List[int]], typing.List[int]]:

            graph = defaultdict(list)

            in_degree = [0] * (k + 1)

            for above, below in conditions:
                graph[above].append(below)
                in_degree[below] += 1
                
            return graph, in_degree
       
        ## A topological sort is where you sort the nodes of a directed graph such that for every edge from node u to node v, u comes before v in the ordering.
        def topological_sort(graph:typing.Dict[int, typing.List[int]], in_degree:typing.List[int]) -> typing.List[int]:
            queue = [i for i in range(1, k + 1) if in_degree[i] == 0]
            order = []
           
            while queue:
                node = queue.pop(0)
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if(in_degree[neighbor] == 0):
                        queue.append(neighbor)
           
            return order if len(order) == k else []
       
        row_graph, row_in_degree = build_graph(rowConditions)
        col_graph, col_in_degree = build_graph(colConditions)
       
        row_order = topological_sort(row_graph, row_in_degree)
        col_order = topological_sort(col_graph, col_in_degree)
       
        if(not row_order or not col_order):
            return []
       
        positions:typing.Dict[int, typing.Tuple[int, int]] = {num: (row_order.index(num), col_order.index(num)) for num in range(1, k + 1)}
       
        matrix:typing.List[typing.List[int]] = [[0] * k for _ in range(k)]

        for num, (row, col) in positions.items():
            matrix[row][col] = num
       
        return matrix
    
## Submission Code:
class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def build_graph(conditions):
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            for above, below in conditions:
                graph[above].append(below)
                in_degree[below] += 1
            return graph, in_degree
        def topological_sort(graph, in_degree):
            queue = [i for i in range(1, k + 1) if in_degree[i] == 0]
            order = []
            while queue:
                node = queue.pop(0)
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == k else []
        row_graph, row_in_degree = build_graph(rowConditions)
        col_graph, col_in_degree = build_graph(colConditions)
        row_order = topological_sort(row_graph, row_in_degree)
        col_order = topological_sort(col_graph, col_in_degree)
        if not row_order or not col_order:
            return []
        positions = {num: (row_order.index(num), col_order.index(num)) for num in range(1, k + 1)}
        matrix = [[0] * k for _ in range(k)]
        for num, (row, col) in positions.items():
            matrix[row][col] = num
        return matrix