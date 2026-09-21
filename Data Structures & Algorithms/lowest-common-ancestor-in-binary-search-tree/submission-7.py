# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while (p.val < root.val and q.val < root.val) or (p.val > root.val and q.val > root.val):
            root = root.left if p.val < root.val else root.right
        return root