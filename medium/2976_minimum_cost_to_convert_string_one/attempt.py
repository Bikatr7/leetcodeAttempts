## Bikatr7
## 2024-07-27
## 2976. Minimum Cost to Convert String I (Medium)

## Description:

## You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters.
## You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost to change the character original[i] to changed[i].
## You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at the cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
## Return the minimum cost to convert the string source to target using any number of operations. If it is impossible to convert source to target, return -1.
## Note that there may exists indices i, j such that original[j] == original[i] and changed[j] == changed[i].

## Constraints:

## 1 <= source.length == target.length <= 10^5
## source, target consist of lowercase English letters.
## 1 <= cost.length == original.length == changed.length <= 2000
## original[i], changed[i] are lowercase English letters.
## 1 <= cost[i] <= 10^6
## original[i] != changed[i]

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def minimumCost(self, source:str, target:str, original:typing.List[str], changed:typing.List[str], cost:typing.List[int]) -> int:
        INFINITY = float('inf')
        graph = [[INFINITY] * 26 for _ in range(26)]

        for i in range(26):
            graph[i][i] = 0
        
        ## Fill the graph with the costs thing
        for original_i, changed_i, cost_i in zip(original, changed, cost):
            original_i, changed_i = ord(original_i) - 97, ord(changed_i) - 97
            graph[original_i][changed_i] = min(graph[original_i][changed_i], cost_i)

        ## Floyd-Warshall algorithm bullshit
        for k in range(26):
            for i in range(26):
                if(graph[i][k] < INFINITY):
                    for j in range(26):
                        new_cost = graph[i][k] + graph[k][j]
                        if(new_cost < graph[i][j]):
                            graph[i][j] = new_cost

        total_cost = 0

        for sourcei, targeti in zip(source, target):
            if(sourcei != targeti):
                cost = graph[ord(sourcei) - 97][ord(targeti) - 97]
                if(cost == INFINITY):
                    return -1
                total_cost += cost

        return total_cost


## Submission Code:
class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = float('inf')
        graph = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for o, c, co in zip(original, changed, cost):
            o, c = ord(o) - 97, ord(c) - 97
            graph[o][c] = min(graph[o][c], co)
        for k in range(26):
            for i in range(26):
                if graph[i][k] < INF:
                    for j in range(26):
                        new_cost = graph[i][k] + graph[k][j]
                        if new_cost < graph[i][j]:
                            graph[i][j] = new_cost
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                cost = graph[ord(s) - 97][ord(t) - 97]
                if cost == INF:
                    return -1
                total_cost += cost
        return total_cost