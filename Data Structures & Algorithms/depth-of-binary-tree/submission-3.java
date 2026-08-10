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
        
        Queue<TreeNode> lvl = new LinkedList<>();

        if(root == null){
            return 0;
        }
        
        lvl.add(root);
        int nodes = 0;


        while (!lvl.isEmpty()){
            System.out.println("New Size: " + String.valueOf(lvl.size()));
            for (TreeNode n: lvl){
                System.out.print(String.valueOf(n.val) + " -> ");
            }
            System.out.println("");
            nodes++;
            int iterate = lvl.size();
            
            for (int i = 0; i < iterate; i++){
                TreeNode c = lvl.remove();
                TreeNode l = c.left;
                TreeNode r = c.right;
                System.out.println("for: " + String.valueOf(i) + " Size: " + String.valueOf(lvl.size()));
                System.out.print("c:" + String.valueOf(c.val));
                if (l != null){
                    lvl.add(l);
                    System.out.print(" l:" + String.valueOf(l.val));
                }
                if (r != null){
                    lvl.add(r);
                    System.out.println(" r:" + String.valueOf(r.val));
                }
            }
            System.out.println("");
        }

        return nodes;

    }
}
