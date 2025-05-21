# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.nodes = 0

    def countNodes(self, root) -> int:
        
        def traverse(self, root):
            if root:
                self.nodes += 1
                traverse(self, root.left)
                traverse(self, root.right)

        traverse(self, root)
        return self.nodes 
