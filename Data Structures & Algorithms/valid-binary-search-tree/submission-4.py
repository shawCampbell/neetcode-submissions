# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(root):
            if not root:
                return -float('infinity'), float('infinity')
            left_max, left_min = dfs(root.left)
            right_max, right_min = dfs(root.right)
            if not (root.val > left_max and root.val < right_min):
                self.res = False
            return max(root.val, max(left_max, right_max)), min(root.val, min(left_min, right_min))

        dfs(root)
        return self.res