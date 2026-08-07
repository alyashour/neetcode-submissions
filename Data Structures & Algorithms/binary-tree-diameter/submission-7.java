/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int maxDiam = 0;

    int heightOf(TreeNode node) {
        if (node == null) return 0;

        int l = heightOf(node.left);
        int r = heightOf(node.right);

        this.maxDiam = Math.max(l + r, this.maxDiam);

        return Math.max(l, r) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        this.heightOf(root);
        return this.maxDiam;
    }
}
