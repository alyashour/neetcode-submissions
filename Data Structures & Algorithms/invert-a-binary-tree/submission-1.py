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

        d = deque()
        d.append(root)

        while len(d) > 0:
            node = d.pop()
            temp = node.right
            node.right = node.left
            node.left = temp

            if node.right is not None:
                d.append(node.right)
            if node.left is not None:
                d.append(node.left)
        
        return root