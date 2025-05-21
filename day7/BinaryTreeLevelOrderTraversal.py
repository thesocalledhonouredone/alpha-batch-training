# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.res = list()

    def levelOrder(self, root):

        if not root:
            return []
        
        q = [root]

        while len(q) != 0:
            qsize = len(q)
            temp = list()

            for _ in range(qsize):
                x = q[0]
                q.remove(x)
                temp.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            self.res.append(temp)
        
        return self.res