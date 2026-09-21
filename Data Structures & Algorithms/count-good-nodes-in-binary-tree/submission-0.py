# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, maxSeen=-float('infinity')):
            if root:
                if root.val >= maxSeen:
                    self.res += 1
                    maxSeen = root.val
                dfs(root.left, maxSeen)
                dfs(root.right, maxSeen)
        dfs(root)
        return self.res