## Bikatr7
## 2024-07-26
## 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium)

## Description:

## There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
## Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
## Notice that the distance between two cities is the sum of the weights of the edges that connect the cities.

## Constraints:

## 2 <= n <= 100
## 1 <= edges.length <= n * (n - 1) / 2
## edges[i].length == 3
## 0 <= fromi < toi < n
## 1 <= weighti, distanceThreshold <= 10^4
## All pairs (fromi, toi) are distinct.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def findTheCity(self, n:int, edges:typing.List[typing.List[int]], distanceThreshold:int) -> int:
        ## Initialize adjacency matrix and fill it with the edge weights
        adjacency_matrix = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
        
        for fromi, toi, weighti in edges:
            adjacency_matrix[fromi][toi] = weighti
            adjacency_matrix[toi][fromi] = weighti
        
        ## Floyd-Warshall algorithm to find the shortest path between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
        
        min_neighbors = n
        city = -1
        
        for i in range(n):
            neighbors = sum(adjacency_matrix[i][j] <= distanceThreshold for j in range(n) if(i != j))
            if(neighbors <= min_neighbors):
                min_neighbors = neighbors
                city = i
        
        return city


## Submission Code:
class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        adjacency_matrix = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
        for fromi, toi, weighti in edges:
            adjacency_matrix[fromi][toi] = weighti
            adjacency_matrix[toi][fromi] = weighti
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
        min_neighbors = n
        city = -1
        for i in range(n):
            neighbors = sum(adjacency_matrix[i][j] <= distanceThreshold for j in range(n) if i != j)
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                city = i
        return city