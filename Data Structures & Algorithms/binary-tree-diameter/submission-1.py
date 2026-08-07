# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def heightOf(node):
            if node is None:
                return 0
            
            l = heightOf(node.left)
            r = heightOf(node.right)

            d = l + r
            self.maxDiam = max(d, self.maxDiam)

            return max(l, r) + 1

        heightOf(root)

        return self.maxDiam

    