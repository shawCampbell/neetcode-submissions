# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(root, lvl=1):
            if root:
                print(root.val)
                if lvl > len(self.res):
                    self.res.append(root.val)
                dfs(root.right, lvl+1)
                dfs(root.left, lvl+1)
        dfs(root)
        return self.res