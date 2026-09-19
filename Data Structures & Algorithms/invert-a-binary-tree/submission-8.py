# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            if cur:
                temp = cur.left
                cur.left = cur.right
                cur.right = temp
                q.append(cur.left)
                q.append(cur.right)
        return root

        # if not root:
        #     return None
        
        # temp = self.invertTree(root.left)
        # root.left = self.invertTree(root.right)
        # root.right = temp

        # return root