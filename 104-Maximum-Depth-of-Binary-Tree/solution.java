/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
            
        } else {
            int leftDepth = maxDepth(root.left)+1;
            int rightDepth = maxDepth(root.right)+1;
            return (leftDepth>rightDepth) ?leftDepth :rightDepth;
            
        }
        
        
    }
}