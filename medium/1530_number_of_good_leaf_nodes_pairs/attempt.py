## Bikatr7
## 2024-07-18
## 1530. Number of Good Leaf Nodes Pairs (Medium)

## Description:

## You are given the root of a binary tree and and integer distance.
## A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
## Return the number of good leaf node pairs in the tree.

## Constraints:

## The number of nodes in the tree is in the range [1, 2^10].
## 1 <= Node.val <= 100
## 1 <= distance <= 10

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root:TreeNode | None, distance:int):
        
        ## Helper function to perform a depth-first search on the binary tree
        def dfs(node:TreeNode | None):
            if(not node):
                return [0] * (distance + 1)
            
            if(not node.left and not node.right):
                leaf_distances = [0] * (distance + 1)
                leaf_distances[1] = 1
                return leaf_distances
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.result += sum(left[l] * right[r] for l in range(distance + 1) for r in range(distance + 1) if l + r <= distance)
            
            return [0] + [left[i] + right[i] for i in range(distance)]
        
        self.result = 0
        dfs(root)

        return self.result
    
## Submission Code:
class Solution:
    def countPairs(self, root, distance):
        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            if not node.left and not node.right:
                leaf_distances = [0] * (distance + 1)
                leaf_distances[1] = 1
                return leaf_distances
            left = dfs(node.left)
            right = dfs(node.right)
            self.result += sum(left[l] * right[r] for l in range(distance + 1) for r in range(distance + 1) if l + r <= distance)
            return [0] + [left[i] + right[i] for i in range(distance)]
        self.result = 0
        dfs(root)
        return self.result