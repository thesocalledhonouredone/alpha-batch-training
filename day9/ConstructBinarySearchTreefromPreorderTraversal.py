# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    pass

class Solution:

    def __init__(self):
        self.i = 0

    def help(self, p, bound):
        if self.i<len(p) and p[self.i] < bound:
            x = p[self.i]
            node = TreeNode(x)
            self.i += 1
            node.left = self.help(p, x)
            node.right = self.help(p, bound)
            return node
    
    def bstFromPreorder(self, preorder):
        return self.help(preorder, float('inf'))
        
