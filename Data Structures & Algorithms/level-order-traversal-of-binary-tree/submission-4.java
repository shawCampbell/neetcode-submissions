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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();

        // **** BFS
        // if (root == null){
        //     return res;
        // }

        // Queue<TreeNode> lvl = new LinkedList<>();
        // lvl.add(root);

        // while (!lvl.isEmpty()){
        //     List<Integer> nodes = new ArrayList<>();
        //     int iterate = lvl.size();
        //     for (int i = 0; i < iterate; i++){
        //         TreeNode node = lvl.remove();
        //         nodes.add(node.val); // FIFO
        //         if (node.left != null){
        //             lvl.add(node.left);
        //         }
        //         if (node.right != null){
        //             lvl.add(node.right);
        //         }
        //     }
        //     res.add(nodes);
        // }

        // return res;

        // **** Recursive DFS 

        if (root == null){
            ;
            return res; // [[]]
        }
        if(root.left == null && root.right == null){
            List<Integer> temp1 = new ArrayList<>();
            temp1.add(root.val);;
            res.add(temp1);
            System.out.println("End: " + res.toString());
            //System.out.println(res.toString());
            return res; //[[4]]
        }
        
        List<Integer> temp1 = new ArrayList<>();
        temp1.add(root.val);;
        res.add(temp1);
        List<List<Integer>> l = levelOrder(root.left);
        List<List<Integer>> r = levelOrder(root.right);
        System.out.println("Must append:");
        System.out.println(l.toString());
        System.out.println(r.toString());
        
        //l.get(0).addAll(r.get(0));
        for (int i = 0; i < r.size(); i++){
            if (i >= l.size()){
                l.add(r.get(i));
            }
            else{
               l.get(i).addAll(r.get(i)); 
            }
            
        }
        res.addAll(l);
        return res;
    }
}
