class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = list()

        for i in s:
            if len(st) == 0 or st[-1] != i:
                st.append(i)
            else:
                st.pop()
        
        return ''.join(st)
    
"""

time complexity : O(n)

"""