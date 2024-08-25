## Kaden Bilyeu (Bikatr7)
## 2024-08-23
## 145. Binary Tree Postorder Traversal (Easy)

## Description:

## Given the root of a binary tree, return the postorder traversal of its nodes' values.

## Example 1:
## Input: root = [1,null,2,3]
## Output: [3,2,1]

## Example 2:
## Input: root = []
## Output: []

## Example 3:
## Input: root = [1]
## Output: [1]

## Constraints:

## The number of the nodes in the tree is in the range [0, 100].
## -100 <= Node.val <= 100

## Topics: Stack, Tree, Depth-First Search, Binary Tree

## Hints:
## 1. Can you think of a recursive solution first?
## 2. For an iterative solution, consider using a stack.
## 3. In postorder traversal, we visit left subtree, then right subtree, and finally the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root):
        if(not root):
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if(node.left):
                stack.append(node.left)
            if(node.right):
                stack.append(node.right)
        
        return result[::-1]
