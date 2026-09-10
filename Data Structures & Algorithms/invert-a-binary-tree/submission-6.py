# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        head = root
        q = deque()
        q.append(root)
        while q:
            root = q.popleft()
            
            if root:
                temp = root.left
                root.left = root.right
                root.right = temp
                
                q.append(root.left)
                q.append(root.right)
        return head
        
        # if not root or (not root.left and not root.right):
        #     return root

        # root.left = self.invertTree(root.left)
        # root.right = self.invertTree(root.right)
        # temp = root.left
        # root.left = root.right
        # root.right = temp 
        # return root