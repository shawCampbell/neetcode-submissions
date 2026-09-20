# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(n):
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            max_height = 1 + max(l, r)
            self.res = max(self.res, l + r)
            return max_height 
        dfs(root)
        return self.res


        
