## Bikatr7
## 2024-07-16
## 1110. Delete Nodes And Return Forest (Medium)

## Description:

## Given the root of a binary tree, each node in the tree has a distinct value.
## After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
## Return the roots of the trees in the remaining forest. You may return the result in any order.

## Constraints:

## The number of nodes in the given tree is at most 1000.
## Each node has a distinct value between 1 and 1000.
## to_delete.length <= 1000
## to_delete contains distinct values between 1 and 1000.

## built-in libraries
import typing

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root:TreeNode, to_delete:typing.List[int]) -> typing.List[TreeNode]:
        
        to_delete = set(to_delete)
        
        remaining_trees = []
        
        def delete_nodes(node:TreeNode | None, is_root):
            
            if(not node):
                return None
            
            is_deleted = node.val in to_delete
            
            ## If the node is the root of a new tree, add it to the list of remaining trees
            if(is_root and not is_deleted):
                remaining_trees.append(node)
            
            ## Recursively delete the left and right children
            node.left = delete_nodes(node.left, is_deleted)
            node.right = delete_nodes(node.right, is_deleted)
            
            ## Return None if the node needs to be deleted
            return None if is_deleted else node
        
        delete_nodes(root, True)
        
        return remaining_trees