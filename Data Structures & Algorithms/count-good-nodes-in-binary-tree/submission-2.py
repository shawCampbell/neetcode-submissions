# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # depth first search
        res = []
        def dfs(root, max_seen):
            if not root:
                return
            max_seen = max(root.val, max_seen)
            if root.val >= max_seen:
                res.append(root.val)
            dfs(root.left, max_seen)
            dfs(root.right, max_seen)

        dfs(root, root.val)
        return len(res)