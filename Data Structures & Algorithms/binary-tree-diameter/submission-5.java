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

    int max(int x, int y) {
        if (x > y) return x;
        else return y;
    }

    int heightOf(TreeNode node) {
        if (node == null) return 0;

        int l = heightOf(node.left);
        int r = heightOf(node.right);

        int diam = l + r;
        this.maxDiam = max(diam, this.maxDiam);

        return max(l, r) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        this.heightOf(root);

        return this.maxDiam;
    }
}
