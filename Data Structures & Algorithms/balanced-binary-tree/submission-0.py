# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(n):
            if not n:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)
            # print(l, r, sep=", ")

            if abs(l - r) > 1:
                self.res = False

            return 1 + max(l, r)

        dfs(root)
        return self.res


            
            
