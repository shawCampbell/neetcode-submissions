# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                # print(None if not cur else cur.val)
                if cur and cur.left:
                    q.append(cur.left)
                if cur and cur.right:
                    q.append(cur.right)
            res.append(cur.val)
        return res
        # self.res = []
        # def dfs(root, lvl=1):
        #     if root:
        #         print(root.val)
        #         if lvl > len(self.res):
        #             self.res.append(root.val)
        #         dfs(root.right, lvl+1)
        #         dfs(root.left, lvl+1)
        # dfs(root)
        # return self.res