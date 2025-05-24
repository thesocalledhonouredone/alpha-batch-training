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
        self.root = None
        # empty BST

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val >= val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        return root

    def myfunc(self,nums, lo, hi):
        if lo > hi:
            return 
        
        mid = (lo + hi) // 2
        self.root = self.insert(self.root, nums[mid])
        self.myfunc(nums, lo, mid-1)
        self.myfunc(nums, mid+1, hi)

    def sortedArrayToBST(self, nums):
        n = len(nums)
        self.myfunc(nums, 0, n-1)
        return self.root
    
"""

Better optimized solution below:

"""

class Another:
    def __init__(self):
        self.root = None
    
    def fun(self, nums, low, high):
        if low > high:
            return None
        m = (low + high) // 2
        node = TreeNode(nums[m])
        node.left = self.fun(nums, low, m-1)
        node.right = self.fun(nums, m+1, high)

        return node

    def sortedArraytToBST(self, nums):
        n = len(nums)
        return self.fun(nums, 0, n-1)