# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        stack.append([root, 1])
        max_l = 1

        while stack:
            cur, l = stack.pop()

            if cur.left:
                stack.append([cur.left, l + 1])
                max_l = max(max_l, l + 1)
            if cur.right:
                stack.append([cur.right, l + 1])
                max_l = max(max_l, l + 1)
                
        return max_l