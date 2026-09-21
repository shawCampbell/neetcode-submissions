# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        p_side = root.left if p.val <= root.val else root.right
        q_side = root.left if q.val <= root.val else root.right

        if p_side != q_side:
            return root

        return self.lowestCommonAncestor(p_side, p, q)