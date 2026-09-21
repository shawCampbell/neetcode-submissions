# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def dfs(n):
            if n:          
                dfs(n.left)
                self.count += 1
                # print(n.val, self.count)
                if self.count == k:
                    self.res = n.val
                dfs(n.right)

        dfs(root)
        return self.res