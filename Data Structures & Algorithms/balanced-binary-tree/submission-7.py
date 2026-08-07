# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def heightOf(node):
            if not node:
                return 0

            l = heightOf(node.left)
            r = heightOf(node.right)
            
            # otherwise
            b = abs(l - r) < 2
            self.isBalanced = self.isBalanced and b

            return max(l, r) + 1

        heightOf(root)
        return self.isBalanced

