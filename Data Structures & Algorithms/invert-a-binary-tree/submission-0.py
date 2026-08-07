# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
            
        return TreeNode(
            root.val, 
            left=None if root.right is None else self.invertTree(root.right) , 
            right=None if root.left is None else self.invertTree(root.left)
        )