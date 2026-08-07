# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def heightOf(node):
            nonlocal maxDiam

            if node is None:
                return 0
            
            l = heightOf(node.left)
            r = heightOf(node.right)

            maxDiam = max(l + r, maxDiam)

            return max(l, r) + 1

        heightOf(root)

        return maxDiam

    