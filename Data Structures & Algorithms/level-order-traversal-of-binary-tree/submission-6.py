# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            lvl = []
            temp = deque()
            while q:
                n = q.popleft()
                if n:
                    lvl.append(n.val)
                    if n.left:
                        temp.append(n.left)
                    if n.right:
                        temp.append(n.right)
            q = temp
            res.append(lvl)
        return res