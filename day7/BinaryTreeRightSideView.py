# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        q = [root]
        res = list()

        while len(q) != 0:
            s = len(q)
            for i in range(s):
                x = q[0]
                q.remove(x)
                if i == s-1: # if i == 0 then it becomes the "left-view" of the tree
                    res.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

        return res