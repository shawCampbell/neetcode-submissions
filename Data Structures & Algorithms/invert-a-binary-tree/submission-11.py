# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative dfs
        q = deque()
        q.append(root)
        while q:
            cur = q.pop()
            if cur:
                temp = cur.right
                cur.right = cur.left
                cur.left = temp
                q.append(cur.left)
                q.append(cur.right)
        
        return root






