# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        q = deque()
        q.append([root,0])
        
        while q:
            root = q.popleft()
            if root[0]:
                if len(res) - 1 < root[1]:
                    res.append([])
                res[root[1]].append(root[0].val)

                q.append([root[0].left, root[1] + 1])
                q.append([root[0].right, root[1] + 1])
        return res
