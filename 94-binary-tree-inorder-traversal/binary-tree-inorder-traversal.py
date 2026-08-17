# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal of a binary tree.
      
        Args:
            root: The root node of the binary tree.
          
        Returns:
            A list containing the values of nodes in inorder sequence.
        """
      
        def traverse_inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse_inorder(node.left)
            result.append(node.val)
            traverse_inorder(node.right)
        result: List[int] = []
        traverse_inorder(root)
        return result
