class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ansMoves = 0
        myst = list()

        for i in s:
            if i == '(':
                myst.append(i)
            elif len(myst) == 0:
                ansMoves += 1
            elif i == ')' and myst[-1]== '(':
                myst.pop()

        return len(myst) + ansMoves


# second approach with counter
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        openc = 0
        closedc = 0

        for i in s:
            if i == '(':
                openc += 1
            elif openc > 0:
                openc -= 1
            else:
                closedc += 1
        
        return openc + closedc
                