# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        b_l = self.isBalanced(root.left)
        b_r = self.isBalanced(root.right)
        if not b_l or not b_r:
            return False
        h_l = self.height(root.left)
        h_r = self.height(root.right)
        diff = abs(h_l - h_r)
        return diff <= 1

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))