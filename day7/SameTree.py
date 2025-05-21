# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.temp = list()

    def traverse(self, root):
        if root:
            self.temp.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)
        else:
            self.temp.append(None)

    def isSameTree(self, p, q) -> bool:

        self.traverse(p)
        parr = self.temp
        self.temp = []
        self.traverse(q)

        return parr == self.temp
    
"""

can be optimized

"""