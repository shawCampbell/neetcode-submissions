# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # validate binary search tree
        def dfs(r, left, right):
            if not r:
                return True
            return (left < r.val < right and
                    dfs(r.left, left, r.val) and
                    dfs(r.right, r.val, right))

        return dfs(root, float('-inf'), float('inf'))
