class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s

        ml = 0
        st = 0

        for i in range(n):
            l = i
            r = i
            while l >= 0 and r<n and s[l] == s[r]:
                if r-l+1 > ml:
                    ml = r-l+1
                    st = 1
                l-= 1
                r+=1
            l, r = i, i+1
            while l >= 0 and r<n and s[l] == s[r]:
                if r-l+1 > ml:
                    ml = r-l+1
                    st = l
                l -= 1
                r += 1
        
        return s[st:ml+1]