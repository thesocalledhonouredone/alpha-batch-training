class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s) == 0:
            return 0

        st = list()

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif len(st) == 0 or s[st[-1]] != '(':
                st.append(i)
            else:
                st.pop()
        
        y = len(s)
        res = 0

        while len(st) != 0:
            res = max(res, y-st[-1]-1)
            y = st[-1]
            st.pop()

        return max(y, res)


"""

Time complexity: O(N)
Space complexity: O(N)

""" 