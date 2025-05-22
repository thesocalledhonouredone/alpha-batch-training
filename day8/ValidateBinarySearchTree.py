# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self, root, lower, upper) -> bool:
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        
        return self.preorder(root.left, lower, root.val) and self.preorder(root.right, root.val, upper)

    def isValidBST(self, root) -> bool:
        return self.preorder(root, -(1 << 31), 1 << 31)