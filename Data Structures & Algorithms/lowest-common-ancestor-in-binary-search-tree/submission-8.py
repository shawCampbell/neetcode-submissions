# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(cn, pn, qn):
            c, p, q = cn.val, pn.val, qn.val
            if (p < c and q < c):
                return dfs(cn.left, pn, qn)
            elif (p > c and q > c):
                return dfs(cn.right, pn, qn)
            else: 
                return cn

        return dfs(root, p, q)
