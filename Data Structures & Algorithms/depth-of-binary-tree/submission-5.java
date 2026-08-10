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
    public int maxDepth(TreeNode root) {
        // BFS
        
        // Queue<TreeNode> lvl = new LinkedList<>();

        // if(root == null){
        //     return 0;
        // }
        
        // lvl.add(root);
        // int nodes = 0;


        // while (!lvl.isEmpty()){
        //     nodes++;
        //     int iterate = lvl.size();
            
        //     for (int i = 0; i < iterate; i++){
        //         TreeNode c = lvl.remove();
        //         TreeNode l = c.left;
        //         TreeNode r = c.right;
        //         if (l != null){
        //             lvl.add(l);
        //         }
        //         if (r != null){
        //             lvl.add(r);
        //         }
        //     }
            
        // }

        // return nodes;

        // **** recursive 

        if(root == null){
            return 0;
        }
        
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
