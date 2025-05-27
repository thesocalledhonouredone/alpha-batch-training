class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i
            # for odd length palindrome

            while l>=0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1


            # for even length palindrome

            l, r = i, i+1

            while l>=0 and r<n and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res