# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(n, bigger=-float('infinity'), smaller=float('infinity')):
            if not n:
                return True
            smaller_l = n.val
            bigger_l = bigger
            smaller_r = smaller
            bigger_r = n.val
            return n.val > bigger and n.val < smaller and dfs(n.left,bigger_l,smaller_l) and dfs(n.right, bigger_r,smaller_r)
            

        return dfs(root)
        # self.res = True
        # def dfs(root):
        #     if not root:
        #         return -float('infinity'), float('infinity')
        #     left_max, left_min = dfs(root.left)
        #     right_max, right_min = dfs(root.right)
        #     if not (root.val > left_max and root.val < right_min):
        #         self.res = False
        #     return max(root.val, max(left_max, right_max)), min(root.val, min(left_min, right_min))

        # dfs(root)
        # return self.res