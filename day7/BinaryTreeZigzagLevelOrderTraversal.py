# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = list()

    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = [root]
        lvl = 1

        while len(q) != 0:
            qs = len(q)
            temp = list()

            for _ in range(qs):
                x = q[0]
                q.remove(x)
                temp.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            if lvl % 2 == 0:
                temp = temp[::-1]
            self.res.append(temp)
            lvl += 1

        return self.res
                