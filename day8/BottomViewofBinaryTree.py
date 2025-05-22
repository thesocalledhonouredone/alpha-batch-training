#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        
        if not root:
            return []
            
        q = [(root, 0)]
        h = dict()
        
        while len(q) != 0:
            
            x = q[0]
            q.remove(x)
            temp, hd = x[0], x[1]
            
            
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