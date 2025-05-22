#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        
        if not root:
            return []
            
        q = [(root, 0)]
        h = dict()
        
        while len(q) != 0:
            
            x = q[0]
            q.remove(x)
            temp, hd = x[0], x[1]
            
            if hd not in h:
                h[hd] = temp.data
            if temp.left:
                q.append((temp.left, hd-1))
            if temp.right:
                q.append((temp.right, hd+1))
        
        
        def findSmallHD(d):
            small = 1000000
            topop = None
            
            for i in d:
                if d[i] < small:
                    topop = i
                    small = d[i]
            
            d.pop(topop)
            return small
                
        res = list()
        for i in h:
            res.append(h[i])
        
        return res
            