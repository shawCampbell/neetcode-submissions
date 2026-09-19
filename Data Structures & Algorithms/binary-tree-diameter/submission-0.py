# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_p = 0
        def max_depth(n):
            if not n:
                return 0

            return 1 + max(max_depth(n.left), max_depth(n.right))

        def max_depths(n):
            nonlocal max_p
            if not n:
                return
            left, right = max_depth(n.left), max_depth(n.right)
            max_p = max(left + right, max_p)

            max_depths(n.left)
            max_depths(n.right)

        max_depths(root)
        return max_p

        
