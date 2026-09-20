# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val

        # q_p, q_q = deque(), deque()
        # q_p.append(p)
        # q_q.append(q)
        # while q_p:
        #     cur_p, cur_q = q_p.popleft(), q_q.popleft()

        #     val_p = None if not cur_p else cur_p.val
        #     val_q = None if not cur_q else cur_q.val

        #     if val_p != val_q:
        #         return False
        #     if cur_p:
        #         q_p.append(cur_p.left)
        #         q_p.append(cur_p.right)
        #     if cur_q:
        #         q_q.append(cur_q.left)
        #         q_q.append(cur_q.right)
        # return True 