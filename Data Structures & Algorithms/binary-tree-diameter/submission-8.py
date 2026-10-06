# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path(root)
        return self.res

    def max_path(self, root):
        if not root:
            return
        max_left = self.max_depth(root.left)
        max_right = self.max_depth(root.right)
        path = max_left + max_right
        self.res = max(self.res, path)
        self.max_path(root.left)
        self.max_path(root.right)
        
    def max_depth(self, n):
        if not n:
            return 0
        return 1 + max(self.max_depth(n.left), self.max_depth(n.right))

        