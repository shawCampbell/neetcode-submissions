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
    public TreeNode invertTree(TreeNode root) {

        // *** iterative BFS 

        // if (root == null){
        //     return root;
        // }

        // Queue<TreeNode> lvl = new LinkedList<>();

        // lvl.add(root);

        // while (!lvl.isEmpty()){
        //     for (int i = 0; i < lvl.size(); i++){
        //         TreeNode c = lvl.remove();
        //         TreeNode l = c.left;
        //         TreeNode r = c.right;
        //         c.left = r;
        //         c.right = l;
        //         if (c.left != null){
        //             lvl.add(c.left);
        //         }
        //         if (c.right != null){
        //             lvl.add(c.right);
        //         }
        //     }
        // }

        // return root;

        // *** recursive 

        //invertTree 

        //boolean end = ((root.left.left == null || root.left == null) && (root.right.right == null || root.right == nul));
        
        if (root == null){
            System.out.println("End: null");
            return root;
        }
        if (root.left == null && root.right == null){
            System.out.println("Root: " + String.valueOf(root.val));
            System.out.println("End: " + String.valueOf(root.val));
            return root;
        }

        System.out.println("Root: " + String.valueOf(root.val));

        TreeNode l = invertTree(root.left);
        TreeNode r = invertTree(root.right);

        root.left = r;
        root.right = l;

        return root;
        
    }
}
