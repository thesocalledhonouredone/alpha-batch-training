#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        
        """
        max overlap for the platform
        
        """
        
        arr.sort()
        dep.sort()
        
        i = j = m = p = 0
        n = len(arr)
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                p += 1
                m = max(p, m)
                i += 1
            else:
                p -= 1
                j += 1
                
        return m
    
    
    
"""

Time Complexity: O(nlogn)

"""