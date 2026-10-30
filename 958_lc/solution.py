# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:

        q = deque([root])
        res = []
        null_seen = False
        while q:
            l = len(q)
            for i in range(l):
                x = q.popleft()
                if x == -1:
                    res.append(-1)
                    continue
                res.append(x.val)
                if x.left:
                    q.append(x.left)
                else:
                    q.append(-1)
                
                if x.right:
                    q.append(x.right)
                else:
                    q.append(-1)

        for x in res:
            if x == -1:
                null_seen = True
            else:
                if null_seen:
                    return False

        return True
        
