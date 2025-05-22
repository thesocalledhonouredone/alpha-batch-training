# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    pass

class Solution:
    def insertIntoBST(self, root, val: int):
        newnode = TreeNode(val)

        if not root:
            return newnode

        t = root
        while True:
            if t.val >= val:
                if t.left is None:
                    t.left = newnode
                    break
                else:
                    t = t.left
            else:
                if t.right is None:
                    t.right = newnode
                    break
                else:
                    t = t.right

        return root