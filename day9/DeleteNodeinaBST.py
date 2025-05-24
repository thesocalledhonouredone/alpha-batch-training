# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMax(self, x):
        while x.right:
            x = x.right
        return x

    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            max_node = self.findMax(root.left)
            root.val = max_node.val
            root.left = self.deleteNode(root.left, max_node.val)

        return root