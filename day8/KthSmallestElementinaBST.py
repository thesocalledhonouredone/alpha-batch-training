# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.c = 0
        self.s = 0

    def inorder(self, root, k) -> None:
        if root:
            self.inorder(root.left, k)
            self.c += 1
            if self.c == k:
                self.s = root.val
                return 
            self.inorder(root.right, k)

    def kthSmallest(self, root, k: int) -> int:

        self.inorder(root, k)
        return self.s
        
